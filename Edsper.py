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

# 声明全局变量
global is_posting
is_posting = 0

# 读取配置文件 ------------------------------------------------
if os.path.exists('config_custom.ini'):
    print('Loading custom config file...')
    cfg_file = 'config_custom.ini'
else:
    print('Loading default config file...')
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

def config_EL():
    pass
    '''
    # 获取已经读取的参数变量
    global eyelink_ip
    global eyelink_sample_rate

    config_EL_window = tk.Toplevel()
    config_EL_window.title('设置 Eyelink 参数')
    
    # 
    ttk.Label(config_EL_window, text="主试机 IP 地址").grid(column=0, row=0, sticky='W', padx=10, pady=6)
    global eyelink_ip_stringVar
    eyelink_ip_stringVar = tk.StringVar(master=config_EL_window)
    eyelink_ip_stringVar.set(eyelink_ip)
    eyelink_ip_entry = ttk.Entry(config_EL_window, width=12, textvariable = eyelink_ip_stringVar)
    eyelink_ip_entry.grid(column=1, row=0, sticky='W', padx=10, pady=6)

    ttk.Label(config_EL_window, text="采样率").grid(column=0, row=1, sticky='W', padx=10, pady=6)
    global eyelink_sample_rate_stringVar
    eyelink_sample_rate_stringVar = tk.StringVar(master=config_EL_window)
    eyelink_sample_rate_stringVar.set(eyelink_sample_rate)
    eyelink_sample_rate_entry = ttk.Combobox(config_EL_window, width=12, textvariable = eyelink_sample_rate_stringVar)
    eyelink_sample_rate_entry['values'] = ('250', '500', '1000', '2000')
    eyelink_sample_rate_entry.grid(column=1, row=1, sticky='W', padx=10, pady=6)
    '''

    def load_eyelink_default():

        global eyelink_ip
        global eyelink_ip_stringVar
        
        global eyelink_sample_rate
        global eyelink_sample_rate_stringVar

        cfg_file = 'config_default.ini'
        cfg_handle = configparser.ConfigParser()
        cfg_handle.read(cfg_file)

        # 设置眼动主试机参数 为 全局变量
        eyelink_ip = cfg_handle.get('eyelink','eyelink_ip')
        eyelink_sample_rate = cfg_handle.get('eyelink','sample_rate')
        eyelink_ip_stringVar.set(eyelink_ip)
        eyelink_sample_rate_stringVar.set(eyelink_sample_rate)

        print('Load custom config file complete.')

    def set_eyelink_properties():

        global eyelink_ip
        global eyelink_ip_stringVar
        
        global eyelink_sample_rate
        global eyelink_sample_rate_stringVar

        cfg_file = 'config_custom.ini'
        cfg_handle = configparser.ConfigParser()
        cfg_handle.read(cfg_file)

        # 设置眼动主试机参数 为 全局变量
        eyelink_ip = eyelink_ip_stringVar.get()
        eyelink_sample_rate = eyelink_sample_rate_stringVar.get()
        
        cfg_handle.set('eyelink', 'eyelink_ip', eyelink_ip)
        cfg_handle.set('eyelink', 'sample_rate', eyelink_sample_rate)
        cfg_handle.write(open("config_custom.ini", "w"))

        print('Load custom config file complete.')

        config_EL_window.destroy()

    load_EL_defualt_button = ttk.Button(config_EL_window,text='加载默认',width=9,command=load_eyelink_default)
    load_EL_defualt_button.grid(column=0,row=2)

    load_EL_defualt_button = ttk.Button(config_EL_window,text='确认',width=9,command=set_eyelink_properties)
    load_EL_defualt_button.grid(column=1,row=2)

    config_EL_window.mainloop()

def config_iMotions():
    pass

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

options_menu = tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label='设置', menu=options_menu)
options_menu.add_command(label='加载配置文件', command=load_ini)
options_menu.add_command(label='保存配置文件', command=save_ini)
options_menu.add_separator()#分割线
options_menu.add_command(label='EyeLink', command=config_EL)
options_menu.add_command(label='iMotions', command=config_iMotions)

# 初始化 el 参数面板 --------------------------------------------------------------------------
monty_el = ttk.LabelFrame(edsper, text='Eyelink')
monty_el.grid(column=0, row=0, padx=8, pady=2)

ttk.Label(monty_el, text="Eyelink IP").grid(column=0, row=0, sticky='W', padx=8, pady=4)
ttk.Label(monty_el, text="Sample Rate").grid(column=0, row=1, sticky='W', padx=8, pady=4)

eyelink_ip_stringVar = tk.StringVar(master = edsper)
eyelink_ip_entry = ttk.Entry(monty_el, width=12, textvariable = eyelink_ip_stringVar)
eyelink_ip_entry.grid(column=1, row=0, sticky='W', padx=8, pady=4)

eyelink_sample_rate_stringVar = tk.StringVar(master = edsper)
eyelink_sample_rate_entry = ttk.Entry(monty_el, width=12, textvariable = eyelink_sample_rate_stringVar)
eyelink_sample_rate_entry.grid(column=1, row=1, sticky='W', padx=8, pady=4)
#---------------------------------------------------------------------------------------------------------#

# 初始化 iMotions 参数面板 --------------------------------------------------------------------------------
monty_im = ttk.LabelFrame(edsper, text='iMotions')
monty_im.grid(column=0, row=1, padx=8, pady=2, rowspan=3)

ttk.Label(monty_im, text="iMotions IP").grid(column=0, row=0, sticky='W', padx=8, pady=4)
ttk.Label(monty_im, text="iMotions Port").grid(column=0, row=1, sticky='W', padx=8, pady=4)

imotions_ip_stringVar = tk.StringVar(master = edsper)
imotions_ip_entry = ttk.Entry(monty_im, width=12, textvariable = imotions_ip_stringVar)
imotions_ip_entry.grid(column=1, row=0, sticky='W', padx=8, pady=4)

imotions_port_stringVar = tk.StringVar(master = edsper)
imotions_port_entry = ttk.Entry(monty_im, width=12, textvariable = imotions_port_stringVar)
imotions_port_entry.grid(column=1, row=1, sticky='W', padx=8, pady=4)
#---------------------------------------------------------------------------------------------------------#

# 初始化 Display 参数面板 --------------------------------------------------------------------------------
monty_display = ttk.LabelFrame(edsper, text='Display')
monty_display.grid(column=1, row=0, padx=8, pady=4, rowspan=2)
# 添加Lable
ttk.Label(monty_display, text="显示器长边").grid(column=1, row=1, sticky='W')
ttk.Label(monty_display, text="显示器短边").grid(column=1, row=2, sticky='W')
ttk.Label(monty_display, text="分辨率(pix)").grid(column=2, row=0, sticky='W')
ttk.Label(monty_display, text="物理尺寸(mm)").grid(column=3, row=0, sticky='W')
# 分辨率 - 长边
display_h_size_pix_stringVar = tk.StringVar()
display_h_size_pix_entry = ttk.Entry(monty_display, width=12, textvariable = display_h_size_pix_stringVar)
display_h_size_pix_entry.grid(column=2, row=1, sticky='W')
# 分辨率 - 短边
display_v_size_pix_stringVar = tk.StringVar()
display_v_size_pix_entry = ttk.Entry(monty_display, width=12, textvariable = display_v_size_pix_stringVar)
display_v_size_pix_entry.grid(column=2, row=2, sticky='W')
# 物理尺寸 - 长边
display_h_size_psysical_stringVar = tk.StringVar()
display_h_size_psysical_entry = ttk.Entry(monty_display, width=12, textvariable = display_h_size_psysical_stringVar)
display_h_size_psysical_entry.grid(column=3, row=1, sticky='W')
# 物理尺寸 - 短边
display_v_size_psysical_stringVar = tk.StringVar()
display_v_size_psysical_entry = ttk.Entry(monty_display, width=12, textvariable = display_v_size_psysical_stringVar)
display_v_size_psysical_entry.grid(column=3, row=2, sticky='W')
#---------------------------------------------------------------------------------------------------------#

# 初始化 Display 参数面板 --------------------------------------------------------------------------------
state_stringVar = tk.StringVar()
state_meaage = ttk.Label(edsper, foreground="green", textvariable = state_stringVar).grid(column=1, row=2, sticky='e',padx=8,pady=1)
state_stringVar.set('欢迎！请先检查硬件参数，再启动转发。')
#---------------------------------------------------------------------------------------------------------#

def click():

    global is_posting

    if is_posting == 0:

        # 使输入框失效
        display_v_size_pix_entry['state']='disable'
        display_h_size_pix_entry['state']='disable'
        display_v_size_psysical_entry['state']='disable'
        display_h_size_psysical_entry['state']='disable'
        imotions_ip_entry['state']='disable'
        imotions_port_entry['state']='disable'
        eyelink_ip_entry['state']='disable'
        eyelink_sample_rate_entry['state']='disable'

        state_stringVar.set('转发中……')
        action['text']='暂停'
        is_posting = 1

    else:
        # 重启输入框
        display_v_size_pix_entry['state']='normal'
        display_h_size_pix_entry['state']='normal'
        display_v_size_psysical_entry['state']='normal'
        display_h_size_psysical_entry['state']='normal'
        imotions_ip_entry['state']='normal'
        imotions_port_entry['state']='normal'
        eyelink_ip_entry['state']='normal'
        eyelink_sample_rate_entry['state']='normal'

        state_stringVar.set('中断')
        action['text']='继续'
        is_posting = 0

# 添加button
action = ttk.Button(edsper,text="转发",width=9,command=click)   
action.grid(column=1,row=3,sticky='e',padx=8,pady=2)

for child in monty_im.winfo_children(): 
    child.grid_configure(padx=3,pady=2)
for child in monty_el.winfo_children(): 
    child.grid_configure(padx=3,pady=2)
for child in monty_display.winfo_children(): 
    child.grid_configure(padx=3,pady=2)

edsper.mainloop()