# To do List ------------------------------------------------
# 每次connect成功时修改lastrun的属性
# 
# -----------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import filedialog
from tkinter import messagebox
import pylink
import socket
import webbrowser
import os
import threading
import configparser

# 声明全局状态变量
global is_posting
is_posting = 0
global is_connected
is_connected = 0
global is_calibrated
is_calibrated = 0
global dummy
dummy = 0

# 声明EL句柄
global EL

# 读取配置文件 ------------------------------------------------
cfg_handle_lastrun = configparser.ConfigParser()
cfg_handle_lastrun.read('lastrun.ini')
try:
    cfg_file = cfg_handle_lastrun.get('lastrun','cnfg_file_name')

    cfg_handle = configparser.ConfigParser()
    cfg_handle.read(cfg_file)

    # 设置被试机参数 为 全局变量
    display_x_res = cfg_handle.get('display','x_res')
    display_y_res = cfg_handle.get('display','y_res')
    display_x_size = cfg_handle.get('display','x_size')
    display_y_size = cfg_handle.get('display','y_size')
    display_distance = cfg_handle.get('display','distance')
    display_ip = cfg_handle.get('display','display_ip')

    # 设置眼动主试机参数 为 全局变量
    eyelink_ip = cfg_handle.get('eyelink','eyelink_ip')
    eyelink_sample_rate = cfg_handle.get('eyelink','sample_rate')

    # 设置imotions参数 为 全局变量
    imotions_ip = cfg_handle.get('imotions','imotions_ip')
    imotions_port = cfg_handle.get('imotions','imotions_port')

    print('Load lastrun config file complete. '+cfg_file)
except:
    if os.path.exists('config_default.ini'):
        cfg_file = 'config_default.ini'

        cfg_handle = configparser.ConfigParser()
        cfg_handle.read(cfg_file)

        # 设置被试机参数 为 全局变量
        display_x_res = cfg_handle.get('display','x_res')
        display_y_res = cfg_handle.get('display','y_res')
        display_x_size = cfg_handle.get('display','x_size')
        display_y_size = cfg_handle.get('display','y_size')
        display_distance = cfg_handle.get('display','distance')
        display_ip = cfg_handle.get('display','display_ip')

        # 设置眼动主试机参数 为 全局变量
        eyelink_ip = cfg_handle.get('eyelink','eyelink_ip')
        eyelink_sample_rate = cfg_handle.get('eyelink','sample_rate')

        # 设置imotions参数 为 全局变量
        imotions_ip = cfg_handle.get('imotions','imotions_ip')
        imotions_port = cfg_handle.get('imotions','imotions_port')

        print('Load custom config file complete. '+cfg_file)

    else:
        # 设置被试机参数 为 全局变量
        display_x_res = 1024
        display_y_res = 768
        display_x_size = 375
        display_y_size = 305
        display_distance = 655
        display_ip = '100.1.1.2'

        # 设置眼动主试机参数 为 全局变量
        eyelink_ip = '100.1.1.1'
        eyelink_sample_rate = 500

        # 设置imotions参数 为 全局变量
        imotions_ip = '127.0.0.1'
        imotions_port = 65535

        print('Load custom config file complete.')
# 配置文件读取完成 ------------------------------------------------

# 创建 instance
edsper = tk.Tk()

# 添加窗口标题
edsper.title('Eyelink Data Stream Poster')

# 关闭resize窗口功能
edsper.resizable(0,0)

# 编辑菜单栏
menubar =tk.Menu(edsper)
edsper.config(menu=menubar)

def load_ini():
    file_name = tk.filedialog.askopenfilename(initialdir = os.getcwd(), filetypes=[('配置文件','.ini')]) 
    cfg_handle = configparser.ConfigParser()
    cfg_handle.read(file_name)

    global display_x_res
    global display_y_res
    global display_x_size
    global display_y_size
    global display_distance
    global display_ip
    global eyelink_ip
    global eyelink_sample_rate
    global imotions_ip
    global imotions_port

    # 设置被试机参数 为 全局变量
    display_x_res = cfg_handle.get('display','x_res')
    display_y_res = cfg_handle.get('display','y_res')
    display_x_size = cfg_handle.get('display','x_size')
    display_y_size = cfg_handle.get('display','y_size')
    display_distance = cfg_handle.get('display','distance')
    display_ip = cfg_handle.get('display','display_ip')

    # 设置眼动主试机参数 为 全局变量
    eyelink_ip = cfg_handle.get('eyelink','eyelink_ip')
    eyelink_sample_rate = cfg_handle.get('eyelink','sample_rate')

    # 设置imotions参数 为 全局变量
    imotions_ip = cfg_handle.get('imotions','imotions_ip')
    imotions_port = cfg_handle.get('imotions','imotions_port')

    print('Load custom config file complete.')

def save_ini():
    
    global display_x_res
    global display_y_res
    global display_x_size
    global display_y_size
    global display_distance
    global display_ip
    global eyelink_ip
    global eyelink_sample_rate
    global imotions_ip
    global imotions_port

    file_name = tk.filedialog.asksaveasfilename(initialdir = os.getcwd(), filetypes=[('配置文件','.ini')]) 
    cfg_handle = configparser.ConfigParser()
    cfg_handle.read('config_default.ini')

    cfg_handle.set('display', 'x_res', display_x_res)
    cfg_handle.set('display', 'y_res', display_y_res)
    cfg_handle.set('display', 'x_size', display_x_size)
    cfg_handle.set('display', 'y_size', display_y_size)
    cfg_handle.set('display', 'distance', display_distance)
    cfg_handle.set('display', 'display_ip', display_ip)

    cfg_handle.set('eyelink', 'eyelink_ip', eyelink_ip)
    cfg_handle.set('eyelink', 'sample_rate', eyelink_sample_rate)

    cfg_handle.set('imotions', 'sample_rate_ip', imotions_ip)
    cfg_handle.set('imotions', 'sample_rate_port', imotions_port)

    cfg_handle.write(open(file_name,'w'))

def set_dummy():
    global dummy
    if dummy == 0:
        dummy = 1
        print('Set as dummy mode.')
    else:
        dummy = 0
        print('Cancel dummy')

options_menu = tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label='设置', menu=options_menu)
dummy_option = options_menu.add_checkbutton(label='Dummy Mode', command=set_dummy)
options_menu.add_separator()
options_menu.add_command(label='加载配置文件', command=load_ini)
options_menu.add_command(label='保存配置文件', command=save_ini)

# 初始化 el 参数面板 --------------------------------------------------------------------------
monty_el = ttk.LabelFrame(edsper, text='Eyelink')
monty_el.grid(column=0, row=0, padx=8, pady=2)

ttk.Label(monty_el, text="Eyelink IP").grid(column=0, row=0, sticky='W', padx=8, pady=4)
ttk.Label(monty_el, text="Sample Rate").grid(column=0, row=1, sticky='W', padx=8, pady=4)

eyelink_ip_stringVar = tk.StringVar(master = edsper)
eyelink_ip_stringVar.set(eyelink_ip)
eyelink_ip_entry = ttk.Entry(monty_el, width=12, textvariable = eyelink_ip_stringVar)
eyelink_ip_entry.grid(column=1, row=0, sticky='W', padx=8, pady=4)

eyelink_sample_rate_stringVar = tk.StringVar(master = edsper)
eyelink_sample_rate_stringVar.set(eyelink_sample_rate)
eyelink_sample_rate_entry = ttk.Combobox(monty_el, width=9, textvariable = eyelink_sample_rate_stringVar)
eyelink_sample_rate_entry['values'] = ('250', '500', '1000', '2000')
eyelink_sample_rate_entry.grid(column=1, row=1, sticky='W', padx=8, pady=4)
#---------------------------------------------------------------------------------------------------------#

# 初始化 iMotions 参数面板 --------------------------------------------------------------------------------
monty_im = ttk.LabelFrame(edsper, text='iMotions')
monty_im.grid(column=0, row=1, padx=8, pady=2, rowspan=3)

ttk.Label(monty_im, text="iMotions IP").grid(column=0, row=0, sticky='W', padx=8, pady=4)
ttk.Label(monty_im, text="iMotions Port").grid(column=0, row=1, sticky='W', padx=8, pady=4)

imotions_ip_stringVar = tk.StringVar(master = edsper)
imotions_ip_stringVar.set(imotions_ip)
imotions_ip_entry = ttk.Entry(monty_im, width=12, textvariable = imotions_ip_stringVar)
imotions_ip_entry.grid(column=1, row=0, sticky='W', padx=8, pady=4)

imotions_port_stringVar = tk.StringVar(master = edsper)
imotions_port_stringVar.set(imotions_port)
imotions_port_entry = ttk.Entry(monty_im, width=12, textvariable = imotions_port_stringVar)
imotions_port_entry.grid(column=1, row=1, sticky='W', padx=8, pady=4)
#---------------------------------------------------------------------------------------------------------#

# 初始化 Display 参数面板 --------------------------------------------------------------------------------
monty_display = ttk.LabelFrame(edsper, text='Display')
monty_display.grid(column=1, row=0, padx=8, pady=4, rowspan=2, columnspan=3)
# 添加Lable
ttk.Label(monty_display, text="显示器长边").grid(column=1, row=1, sticky='W')
ttk.Label(monty_display, text="显示器短边").grid(column=1, row=2, sticky='W')
ttk.Label(monty_display, text="分辨率(pix)").grid(column=2, row=0, sticky='W')
ttk.Label(monty_display, text="物理尺寸(mm)").grid(column=3, row=0, sticky='W')
# 分辨率 - 长边
display_x_size_pix_stringVar = tk.StringVar()
display_x_size_pix_stringVar.set(display_x_res)
display_x_size_pix_entry = ttk.Entry(monty_display, width=12, textvariable = display_x_size_pix_stringVar)
display_x_size_pix_entry.grid(column=2, row=1, sticky='W')
# 分辨率 - 短边
display_y_size_pix_stringVar = tk.StringVar()
display_y_size_pix_stringVar.set(display_y_res)
display_y_size_pix_entry = ttk.Entry(monty_display, width=12, textvariable = display_y_size_pix_stringVar)
display_y_size_pix_entry.grid(column=2, row=2, sticky='W')
# 物理尺寸 - 长边
display_x_size_psysical_stringVar = tk.StringVar()
display_x_size_psysical_stringVar.set(display_x_size)
display_x_size_psysical_entry = ttk.Entry(monty_display, width=12, textvariable = display_x_size_psysical_stringVar)
display_x_size_psysical_entry.grid(column=3, row=1, sticky='W')
# 物理尺寸 - 短边
display_y_size_psysical_stringVar = tk.StringVar()
display_y_size_psysical_stringVar.set(display_y_size)
display_y_size_psysical_entry = ttk.Entry(monty_display, width=12, textvariable = display_y_size_psysical_stringVar)
display_y_size_psysical_entry.grid(column=3, row=2, sticky='W')
#---------------------------------------------------------------------------------------------------------#

# 初始化 Display 参数面板 --------------------------------------------------------------------------------
state_stringVar = tk.StringVar()
state_meaage = ttk.Label(edsper, foreground="green", textvariable = state_stringVar).grid(column=1, row=2, columnspan=3, sticky='e', padx=8, pady=1)
state_stringVar.set('欢迎！请先检查硬件参数，再启动转发。')
#---------------------------------------------------------------------------------------------------------#

def post_data():

    global is_posting

    if is_posting == 0:

        state_stringVar.set('转发中……')
        post_button['text']='暂停'
        is_posting = 1

    else:

        state_stringVar.set('中断')
        post_button['text']='继续'
        is_posting = 0

def connect():
    
    global EL
    global is_connected

    if is_connected == 0:
        if dummy == 0:
            try:
                print('Try to connect to Eyelink.')
                EL = pylink.EyeLink(str(eyelink_ip))

                # 使输入框失效
                display_y_size_pix_entry['state']='disable'
                display_x_size_pix_entry['state']='disable'
                display_y_size_psysical_entry['state']='disable'
                display_x_size_psysical_entry['state']='disable'
                imotions_ip_entry['state']='disable'
                imotions_port_entry['state']='disable'
                eyelink_ip_entry['state']='disable'
                eyelink_sample_rate_entry['state']='disable'

                cal_button['state']='normal'
                post_button['state']='normal'

                connect_button['text']='断开连接'
                is_connected = 1
            except:
                state_stringVar.set('连接失败')
        else: # dummy = 1
            state_stringVar.set('Dummy Mode')
            # 使输入框失效
            display_y_size_pix_entry['state']='disable'
            display_x_size_pix_entry['state']='disable'
            display_y_size_psysical_entry['state']='disable'
            display_x_size_psysical_entry['state']='disable'
            imotions_ip_entry['state']='disable'
            imotions_port_entry['state']='disable'
            eyelink_ip_entry['state']='disable'
            eyelink_sample_rate_entry['state']='disable'

            post_button['state']='normal'
    else:
        # 重启输入框
        display_y_size_pix_entry['state']='normal'
        display_x_size_pix_entry['state']='normal'
        display_y_size_psysical_entry['state']='normal'
        display_x_size_psysical_entry['state']='normal'
        imotions_ip_entry['state']='normal'
        imotions_port_entry['state']='normal'
        eyelink_ip_entry['state']='normal'
        eyelink_sample_rate_entry['state']='normal'

        cal_button['state']='disable'
        post_button['state']='disable'
        connect_button['text']='连接'
        is_connected = 0

def cal_el():
    pass

# 添加button
connect_button = ttk.Button(edsper,text="连接",width=9,command=connect)   
connect_button.grid(column=1,row=3,sticky='e',padx=8,pady=2)

cal_button = ttk.Button(edsper,text="校准",width=9,command=cal_el)   
cal_button.grid(column=2,row=3,sticky='e',padx=8,pady=2)
cal_button['state']='disable'

post_button = ttk.Button(edsper,text="转发",width=9,command=post_data)   
post_button.grid(column=3,row=3,sticky='e',padx=8,pady=2)
post_button['state']='disable'

for child in monty_im.winfo_children(): 
    child.grid_configure(padx=3,pady=2)
for child in monty_el.winfo_children(): 
    child.grid_configure(padx=3,pady=2)
for child in monty_display.winfo_children(): 
    child.grid_configure(padx=3,pady=2)

edsper.mainloop()