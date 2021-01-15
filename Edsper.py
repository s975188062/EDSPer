import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import filedialog
from tkinter import messagebox
from math import sin
from math import cos
from math import tan
from math import pi
from math import radians
from tkinter.constants import COMMAND
import pylink
import socket
import webbrowser
import os
import threading
import configparser


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
eyelink_ip = cfg_handle.get('eyelink','host_ip')
eyelink_sample_rate = cfg_handle.get('eyelink','sample_rate')

# 设置imotions参数 为 全局变量
imotions_ip = cfg_handle.get('imotions','imotions_ip')
imotions_port = cfg_handle.get('imotions','imotions_port')

print('Load custom config file complete.')
# 配置文件读取完成 ------------------------------------------------

# 创建 instance
esper = tk.Tk()

# 添加窗口标题
esper.title('Eyelink Data Stream Poster')

# 关闭resize窗口功能
esper.resizable(0,0)

# 编辑菜单栏
menubar =tk.Menu(esper)
esper.config(menu=menubar)

def config_EL():

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

    def load_eyelink_default():

        global eyelink_ip
        global eyelink_ip_stringVar
        
        global eyelink_sample_rate
        global eyelink_sample_rate_stringVar

        cfg_file = 'config_default.ini'
        cfg_handle = configparser.ConfigParser()
        cfg_handle.read(cfg_file)

        # 设置眼动主试机参数 为 全局变量
        eyelink_ip = cfg_handle.get('eyelink','host_ip')
        eyelink_sample_rate = cfg_handle.get('eyelink','sample_rate')
        eyelink_ip_stringVar.set(eyelink_ip)
        eyelink_sample_rate_stringVar.set(eyelink_sample_rate)

        print('Load custom config file complete.')

    load_EL_defualt_button = ttk.Button(config_EL_window,text='加载默认',width=9,command=load_eyelink_default)
    load_EL_defualt_button.grid(column=0,row=2)

    config_EL_window.mainloop()

def config_iMotions():
    global imotions_ip
    print(imotions_ip)
    pass

options_menu = tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label='设置', menu=options_menu)
options_menu.add_command(label='EyeLink', command=config_EL)
options_menu.add_command(label='iMotions', command=config_iMotions)

device_monty = ttk.LabelFrame(esper, text='请先设置硬件参数，再执行数据转发。\nPlease Set Attributes First Before Post.')
device_monty.grid(column=0, row=0, padx=8, pady=4)

tabControl = ttk.Notebook(esper) 
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='字号计算器')   

ttk.Label(tab1, text="显示器长边").grid(column=1, row=1, sticky='W')

#---------------------------------------------------------------------------------------------------------#

# 添加Lable
ttk.Label(device_monty, text="显示器长边").grid(column=1, row=1, sticky='W')
ttk.Label(device_monty, text="显示器短边").grid(column=1, row=2, sticky='W')
ttk.Label(device_monty, text="分辨率(pix)").grid(column=2, row=0, sticky='W')
ttk.Label(device_monty, text="物理尺寸(mm)").grid(column=3, row=0, sticky='W')
ttk.Label(device_monty, text="被试到显示器的距离(mm)").grid(column=1, row=3, columnspan=2, sticky='W')


# 添加输入框 ---------------------------------------------------------------
# 物理尺寸 - 长边
Num_of_Long_Length_1 = tk.StringVar()
Num_of_Long_Length_Entered_1 = ttk.Entry(device_monty, width=12, textvariable = Num_of_Long_Length_1)
Num_of_Long_Length_Entered_1.grid(column=3, row=1, sticky='W')

# 物理尺寸 - 短边
Num_of_Short_Length_1 = tk.StringVar()
Num_of_Short_Length_Entered_1 = ttk.Entry(device_monty, width=12, textvariable = Num_of_Short_Length_1)
Num_of_Short_Length_Entered_1.grid(column=3, row=2, sticky='W')

# 分辨率 - 长边
Num_of_Long_Resolution_1 = tk.StringVar()
Num_of_Long_Resolution_Entered_1 = ttk.Entry(device_monty, width=12, textvariable = Num_of_Long_Resolution_1)
Num_of_Long_Resolution_Entered_1.grid(column=2, row=1, sticky='W')

# 分辨率 - 短边
Num_of_Short_Resolution_1 = tk.StringVar()
Num_of_Short_Resolution_Entered_1 = ttk.Entry(device_monty, width=12, textvariable = Num_of_Short_Resolution_1)
Num_of_Short_Resolution_Entered_1.grid(column=2, row=2, sticky='W')

# 被试到显示器的距离
Num_of_Distance_to_Screen_1 = tk.StringVar()
Num_of_Distance_to_Screen_Entered_1 = ttk.Entry(device_monty, width=12, textvariable = Num_of_Distance_to_Screen_1)
Num_of_Distance_to_Screen_Entered_1.grid(column=3, row=3, sticky='W')

# 单位视角的字符个数
Num_of_letters_per_angle = tk.StringVar()
Num_of_letters_per_angle_Entered = ttk.Entry(device_monty, width=12, textvariable = Num_of_letters_per_angle)
Num_of_letters_per_angle_Entered.grid(column=3, row=4, sticky='W')
# 添加输入框 ---------------------------------------------------------------

# Adding a Combobox
letter_type = tk.StringVar()
letter_type_Chosen = ttk.Combobox(device_monty, width=8, textvariable=letter_type)
letter_type_Chosen['values'] = ('中文', '英文')
letter_type_Chosen.grid(column=2, row=4)
letter_type_Chosen.current(0)  #设置初始显示值，值为元组['values']的下标
letter_type_Chosen.config(state='readonly')  #设为只读模式

# 添加button
action = ttk.Button(device_monty,text="转发\nPost",width=9)   
action.grid(column=3,row=5,rowspan=2)


for child in device_monty.winfo_children(): 
    child.grid_configure(padx=3,pady=1)



esper.mainloop()