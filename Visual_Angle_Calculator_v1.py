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
import webbrowser
import os

# 创建 instance
vac = tk.Tk()

# 添加窗口标题
vac.title('Visual Angle Calcuator - v1.0')

# 关闭resize窗口功能
vac.resizable(0,0)

'''
#修改关闭窗口函数
def Close_Window():
    
    global vac
    vac.destroy()

    os.remove('tips.gif')
vac.protocol('WM_DELETE_WINDOW', Close_Window)
'''

# 编辑菜单栏
menubar =tk.Menu(vac)
vac.config(menu=menubar)

def Show_Help():#
    Help_Window = tk.Toplevel()
    Help_Window.title('帮助窗口')
    #Help_Window.geometry("800x600")

    Help_tabControl = ttk.Notebook(Help_Window)          # Create Tab Control
 
    Help_tab1 = ttk.Frame(Help_tabControl)            # Create a tab 
    Help_tabControl.add(Help_tab1, text='字号计算器')             # Add the tab

    Help_tab2 = ttk.Frame(Help_tabControl)            # Add a second tab
    Help_tabControl.add(Help_tab2, text='环形排列计算器')             # Make second tab visible

    Help_tab3 = ttk.Frame(Help_tabControl)            # Add a forth tab
    Help_tabControl.add(Help_tab3, text='Message Savior')      # Make second tab visible
    
    Help_tabControl.pack(expand=1, fill="both")      # Pack to make visible

    # 字号计算器的帮助内容
    Help_1_monty = ttk.LabelFrame(Help_tab1, text='使用方法：')
    Help_1_monty.grid(column=0, row=0, padx=8, pady=4)
    Help_tab1_str = ['1. 填入显示器的分辨率，注意要跟程序设计的分辨率一致；', \
                     '2. 填入显示器显示范围的屋里尺寸，单位是“毫米”；', \
                     '3. 填入被试眼睛到显示器的直线距离，单位是“毫米”；', \
                     '4. 选择“中文”或者“英文”，填入单位视角内的字符个数；', \
                     '5. 点击“计算”。']
    for xx in range(len(Help_tab1_str)):
        ttk.Label(Help_1_monty, text=Help_tab1_str[xx]).grid(column=0, row=xx, sticky='W')

    # 环形排列计算器的帮助内容
    Help_2_monty_Single = ttk.LabelFrame(Help_tab2, text='单Target使用方法：')
    Help_2_monty_Single.grid(column=0, row=0, padx=8, pady=4)
    Help_tab2_str_Single = ['1. 填入显示器的分辨率，注意要跟程序设计的分辨率一致；', \
                            '2. 填入显示器显示范围的屋里尺寸，单位是“毫米”；', \
                            '3. 填入被试眼睛到显示器的直线距离，单位是“毫米”；', \
                            '4. Target Count填“1”；', \
                            '5. Target的大小，水平竖直方向各占多大视角，单位为“度”；', \
                            '6. 环绕半径，填入Target距屏幕中心的视角距离，单位为“度”；', \
                            '7. 以0点方向为0，顺时针方向为正，填入Target在表盘上的方向，单位为“度”。   ']
    for xx in range(len(Help_tab2_str_Single)):
        ttk.Label(Help_2_monty_Single, text=Help_tab2_str_Single[xx]).grid(column=0, row=xx, sticky='W')
    
    Help_2_monty_Mutiple = ttk.LabelFrame(Help_tab2, text='多Target使用方法：')
    Help_2_monty_Mutiple.grid(column=0, row=1, padx=8, pady=4)
    Help_tab2_str_Mutiple = ['1. 填入显示器的分辨率，注意要跟程序设计的分辨率一致；', \
                             '2. 填入显示器显示范围的屋里尺寸，单位是“毫米”；', \
                             '3. 填入被试眼睛到显示器的直线距离，单位是“毫米”；', \
                             '4. 填入Target的数量；', \
                             '5. Target的大小，水平竖直方向各占多大视角，单位为“度”；', \
                             '6. 填入环绕半径，即所有Target以多大的半径排列在屏幕上，单位为“度”。', \
                             '7. 填入顺时针偏移角度，单位为“度”，若不需要旋转则填“0”。默认第一个Target在', \
                             '   正上方，即表盘上0点的方向。顺时针为正方向，若需要顺时针旋转所有Target20', \
                             '   度，则填入“20”。若需要逆时针旋转所有Target20度，则填入“-20”。']
    for xx in range(len(Help_tab2_str_Mutiple)):
        ttk.Label(Help_2_monty_Mutiple, text=Help_tab2_str_Mutiple[xx]).grid(column=0, row=xx, sticky='W')
    
    # Message Savior的帮助内容
    Help_3_monty = ttk.LabelFrame(Help_tab3, text='使用方法：')
    Help_3_monty.grid(column=0, row=0, padx=8, pady=4)
    Help_tab3_str = ['首先明确一件最重要的事，该脚本只能适用于EB编写程序的Message补救。', \
                     '打开数据文件夹中的eb_message.log文件，到里面寻找对应的控件名称。', \
                     '以一个简单的DisplayScreen_Action+Timer_Trigger为例：', \
                     '在eb_message.log文件中存在类似如下内容：', \
                     '  13798.494 DRIFT_CORRECT Blocks.Trials.DRIFT_CORRECT', \
                     '  15515.543 Stim Blocks.Trials.Recording.DisplayScreen (BEGIN) ', \
                     '  15522.778 Stim Blocks.Trials.Recording.DisplayScreen', \
                     '  15582.065 TIMER Blocks.Trials.Recording.TIMER', \
                     '  15611.742 ADD_TO_RESULTS_FILE Blocks.Trials.ADD_TO_RESULTS_FILE', \
                     '我们可以从中看到DisplayScreen (BEGIN), DisplayScreen, 和Timer。', \
                     '其中DisplayScreen(Begin)是准备显示，DisplayScreen是显示，Timer是计时', \
                     '结束。我们要找的就是DisplayScreen和Timer，因此将文字部分全部输入到框中，', \
                     '以此为例，具体操作方法如下：\n', \
                     '1. 点击“Load file”，找到eb_message.log文件，点击确定。；', \
                     '2. 在第1行左侧输入“Stim Blocks.Trials.Recording.DisplayScreen”，右侧输入“Stim”；', \
                     '3. 在第2行左侧输入“TIMER Blocks.Trials.Recording.TIMER”，右侧输入“Timer”；', \
                     '4. 点击“Run”，在eb_message.log的相同路径下会产生一个叫做msg_add.txt的新文件', \
                     '5. 在DV中对应edf的数据名称将msg_add.txt重新加载接即可。']
    for xx in range(len(Help_tab3_str)):
        ttk.Label(Help_3_monty, text=Help_tab3_str[xx]).grid(column=0, row=xx, sticky='W')

def More_Help():
    tk.messagebox.showinfo('提示','更多信息和讨论请Email至charlie-techblog@outlook.com！')

def reward_charlie():
    webbrowser.open("http://charlie-techblog.com/reward_charlie/")

menu1=tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label='帮助', menu=menu1)
menu1.add_command(label='使用方法', command=Show_Help)
menu1.add_command(label='更多帮助', command=More_Help)
menu1.add_command(label='赞赏Charlie', command=reward_charlie)

# Tab Control introduced here --------------------------------------
tabControl = ttk.Notebook(vac)          # Create Tab Control
 
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='字号计算器')             # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='环形排列计算器')             # Make second tab visible
 
#tab3 = ttk.Frame(tabControl)            # Add a third tab
#tabControl.add(tab3, text='大小计算器')             # Make second tab visible

tab3 = ttk.Frame(tabControl)            # Add a forth tab
tabControl.add(tab3, text='Message Savior')      # Make second tab visible
 
tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ~ Tab Control introduced here -----------------------------------------

#---------------Tab1控件介绍------------------#
# We are creating a container tab3 to hold all other widgets
monty = ttk.LabelFrame(tab1, text='本计算器仅用作参考，请输入数值信息：')
monty.grid(column=0, row=0, padx=8, pady=4)

# 定义按钮点击函数
def clickMe():

    if (Num_of_Long_Length_1.get() == '') | \
        (Num_of_Short_Length_1.get() == '') | \
        (Num_of_Long_Resolution_1.get() == '') | \
        (Num_of_Short_Resolution_1.get() == '') | \
        (Num_of_Distance_to_Screen_1.get() == '') | \
        (Num_of_letters_per_angle.get() == ''):#确定所有输入框都填入了内容

        tk.messagebox.showinfo('错误','Aha！数值要填全呦！')
    
    else:
        L_len_1 = float(Num_of_Long_Length_1.get())         #获取屏幕长边物理尺寸
        S_len_1 = float(Num_of_Short_Length_1.get())        #获取屏幕短边物理尺寸
        L_res_1 = float(Num_of_Long_Resolution_1.get())     #获取屏幕长边分辨率
        S_res_1 = float(Num_of_Short_Resolution_1.get())    #获取屏幕短边分辨率
        dstc_1 = float(Num_of_Distance_to_Screen_1.get())   #获取眼睛到屏幕的距离
        nlpva = float(Num_of_letters_per_angle.get())   #获取单位视角的字符个数
        if letter_type_Chosen.get() == '中文':
            pont_size = round(0.75*tan(pi/(180*nlpva))*dstc_1*(L_res_1/L_len_1), 1)
        else:
            pont_size = round(0.75*2*tan(pi/(180*nlpva))*dstc_1*(L_res_1/L_len_1), 1)
        tk.messagebox.showinfo('Result',(str(pont_size) + letter_type_Chosen.get()))

# 添加Lable
ttk.Label(monty, text="显示器长边").grid(column=1, row=1, sticky='W')
ttk.Label(monty, text="显示器短边").grid(column=1, row=2, sticky='W')
ttk.Label(monty, text="分辨率(pix)").grid(column=2, row=0, sticky='W')
ttk.Label(monty, text="物理尺寸(mm)").grid(column=3, row=0, sticky='W')
ttk.Label(monty, text="被试到显示器的距离(mm)").grid(column=1, row=3, columnspan=2, sticky='W')
ttk.Label(monty, text="每度视角字符个数").grid(column=1, row=4, sticky='W')

# 添加输入框 ---------------------------------------------------------------
# 物理尺寸 - 长边
Num_of_Long_Length_1 = tk.StringVar()
Num_of_Long_Length_Entered_1 = ttk.Entry(monty, width=12, textvariable = Num_of_Long_Length_1)
Num_of_Long_Length_Entered_1.grid(column=3, row=1, sticky='W')

# 物理尺寸 - 短边
Num_of_Short_Length_1 = tk.StringVar()
Num_of_Short_Length_Entered_1 = ttk.Entry(monty, width=12, textvariable = Num_of_Short_Length_1)
Num_of_Short_Length_Entered_1.grid(column=3, row=2, sticky='W')

# 分辨率 - 长边
Num_of_Long_Resolution_1 = tk.StringVar()
Num_of_Long_Resolution_Entered_1 = ttk.Entry(monty, width=12, textvariable = Num_of_Long_Resolution_1)
Num_of_Long_Resolution_Entered_1.grid(column=2, row=1, sticky='W')

# 分辨率 - 短边
Num_of_Short_Resolution_1 = tk.StringVar()
Num_of_Short_Resolution_Entered_1 = ttk.Entry(monty, width=12, textvariable = Num_of_Short_Resolution_1)
Num_of_Short_Resolution_Entered_1.grid(column=2, row=2, sticky='W')

# 被试到显示器的距离
Num_of_Distance_to_Screen_1 = tk.StringVar()
Num_of_Distance_to_Screen_Entered_1 = ttk.Entry(monty, width=12, textvariable = Num_of_Distance_to_Screen_1)
Num_of_Distance_to_Screen_Entered_1.grid(column=3, row=3, sticky='W')

# 单位视角的字符个数
Num_of_letters_per_angle = tk.StringVar()
Num_of_letters_per_angle_Entered = ttk.Entry(monty, width=12, textvariable = Num_of_letters_per_angle)
Num_of_letters_per_angle_Entered.grid(column=3, row=4, sticky='W')
# 添加输入框 ---------------------------------------------------------------

# Adding a Combobox
letter_type = tk.StringVar()
letter_type_Chosen = ttk.Combobox(monty, width=8, textvariable=letter_type)
letter_type_Chosen['values'] = ('中文', '英文')
letter_type_Chosen.grid(column=2, row=4)
letter_type_Chosen.current(0)  #设置初始显示值，值为元组['values']的下标
letter_type_Chosen.config(state='readonly')  #设为只读模式

# 添加button
action = ttk.Button(monty,text="计算",width=9,command=clickMe)   
action.grid(column=3,row=5,rowspan=2)


for child in monty.winfo_children(): 
    child.grid_configure(padx=3,pady=1)
#---------------Tab1控件介绍结束------------------#
#------------------------------------------------------------------------------------------------------------------------------------
#---------------Tab2控件介绍开始------------------#
# We are creating a container tab3 to hold all other widgets
monty2 = ttk.LabelFrame(tab2, text='本计算器仅用作参考，请输入数值信息：')
monty2.grid(column=0, row=0, padx=8, pady=4)

def Calculate_2():
    if (Num_of_Long_Length.get() == '') | \
        (Num_of_Short_Length.get() == '') | \
        (Num_of_Long_Resolution.get() == '') | \
        (Num_of_Short_Resolution.get() == '') | \
        (Num_of_Distance_to_Screen.get() == '') | \
        (Num_of_Target_Count.get() == '') | \
        (Num_of_Target_Size_Long_Side.get() == '') | \
        (Num_of_Target_Size_Short_Side.get() == '') | \
        (Layout_Radius.get() == '') | \
        (Clockwise_Deflection_Angle.get() == ''):#确定所有输入框都填入了内容

        tk.messagebox.showinfo('错误','Aha！数值要填全呦！')

    else:
        L_len = float(Num_of_Long_Length.get())                             #获取屏幕长边物理尺寸
        S_len = float(Num_of_Short_Length.get())                            #获取屏幕短边物理尺寸
        L_res = float(Num_of_Long_Resolution.get())                         #获取屏幕长边分辨率
        S_res = float(Num_of_Short_Resolution.get())                        #获取屏幕短边分辨率
        dstc = float(Num_of_Distance_to_Screen.get())                       #获取眼睛到屏幕的距离
        Tgt_Count = int(Num_of_Target_Count.get())                          #获取Target数量
        Tgt_S_L = radians(float(Num_of_Target_Size_Long_Side.get()))        #获取Target水平大小
        Tgt_S_S = radians(float(Num_of_Target_Size_Short_Side.get()))       #获取Target竖直大小
        Lyt_Raidus = radians(float(Layout_Radius.get()))                    #获取排列半径
        Lyt_Deflection = radians(float(Clockwise_Deflection_Angle.get()))   #获取顺时针偏转方向

        Angle_List = list(range(Tgt_Count))#创建Target的表盘方向数组（0-2pi，正上方为0，顺时针）
        Tgt_List_Output = []
        for index in range(Tgt_Count):  #依次计算所有Tgt
            Angle_List[index] = Lyt_Deflection + 2 * pi * index / Tgt_Count   #当前Tgt的偏转角度
            Tgt_Position_Raidus_by_Long  = dstc * tan(Lyt_Raidus) * (L_res / L_len)      #计算排列半径对应的像素值
            Tgt_Position_Raidus_by_Short = dstc * tan(Lyt_Raidus) * (S_res / S_len)
            Tgt_Position_x = int((L_res / 2 + Tgt_Position_Raidus_by_Long * sin(Angle_List[index])))   #计算x方向上的坐标
            Tgt_Position_y = int((S_res / 2 - Tgt_Position_Raidus_by_Short * cos(Angle_List[index])))   #计算y方向上的坐标
            Tgt_Size_x = int(dstc * (tan(Lyt_Raidus + Tgt_S_L / 2) - tan(Lyt_Raidus - Tgt_S_L / 2)) * (L_res / L_len))
            Tgt_Size_y = int(dstc * (tan(Lyt_Raidus + Tgt_S_S / 2) - tan(Lyt_Raidus - Tgt_S_S / 2)) * (S_res / S_len))
            Output = [('Target_' + str(index + 1)), str(Tgt_Position_x), str(Tgt_Position_y), str(Tgt_Size_x), str(Tgt_Size_y)]    
            Tgt_List_Output.append(Output)

        # 数据显示
        Result_Window = tk.Toplevel()
        Result_Window.title('计算结果')
        tree = ttk.Treeview(Result_Window)      # #创建表格对象
        tree['columns'] = ('Position', 'Size')     # #定义列
        tree.column('Position' , width=100)          # #设置列
        tree.column('Size',      width=100)
        tree.heading('Position', text='坐标')        # #设置显示的表头名
        tree.heading('Size',     text='大小')
        for index in range(Tgt_Count):
            tree.insert('', index, text=Tgt_List_Output[index][0], values=(\
                ('[' + Tgt_List_Output[index][1] + ',' + Tgt_List_Output[index][2] + ']'), \
                (Tgt_List_Output[index][3] + 'x' + Tgt_List_Output[index][4])))
        tree.pack()

# 添加Lable
ttk.Label(monty2, text="显示器长边").grid(column=1, row=1, sticky='W')
ttk.Label(monty2, text="显示器短边").grid(column=1, row=2, sticky='W')
ttk.Label(monty2, text="分辨率(pix)").grid(column=2, row=0, sticky='W')
ttk.Label(monty2, text="物理尺寸(mm)").grid(column=3, row=0, sticky='W')
ttk.Label(monty2, text="被试到显示器的距离(mm)").grid(column=1, row=3, sticky='W')
ttk.Label(monty2, text="Target Count").grid(column=1, row=4, sticky='W')
ttk.Label(monty2, text="Target Size 水平｜竖直").grid(column=1, row=5, sticky='W')
ttk.Label(monty2, text="环绕半径").grid(column=1, row=6, sticky='W')
ttk.Label(monty2, text="顺时针偏移角度").grid(column=1, row=7, sticky='W')

# 添加输入框
# 物理尺寸 - 长边
Num_of_Long_Length = tk.StringVar()
Num_of_Long_Length_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Long_Length)
Num_of_Long_Length_Entered.grid(column=3, row=1, sticky='W')

# 物理尺寸 - 短边
Num_of_Short_Length = tk.StringVar()
Num_of_Short_Length_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Short_Length)
Num_of_Short_Length_Entered.grid(column=3, row=2, sticky='W')

# 分辨率 - 长边
Num_of_Long_Resolution = tk.StringVar()
Num_of_Long_Resolution_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Long_Resolution)
Num_of_Long_Resolution_Entered.grid(column=2, row=1, sticky='W')

# 分辨率 - 短边
Num_of_Short_Resolution = tk.StringVar()
Num_of_Short_Resolution_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Short_Resolution)
Num_of_Short_Resolution_Entered.grid(column=2, row=2, sticky='W')

# 被试到显示器的距离
Num_of_Distance_to_Screen = tk.StringVar()
Num_of_Distance_to_Screen_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Distance_to_Screen)
Num_of_Distance_to_Screen_Entered.grid(column=2, row=3, sticky='W')

# Target_Count
Num_of_Target_Count = tk.StringVar()
Num_of_Target_Count_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Target_Count)
Num_of_Target_Count_Entered.grid(column=2, row=4, sticky='W')

# Target_Size
Num_of_Target_Size_Long_Side = tk.StringVar()
Num_of_Target_Size_Long_Side_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Target_Size_Long_Side)
Num_of_Target_Size_Long_Side_Entered.grid(column=2, row=5, sticky='W')

Num_of_Target_Size_Short_Side = tk.StringVar()
Num_of_Target_Size_Short_Side_Entered = ttk.Entry(monty2, width=12, textvariable = Num_of_Target_Size_Short_Side)
Num_of_Target_Size_Short_Side_Entered.grid(column=3, row=5, sticky='W')

# 环绕直径
Layout_Radius = tk.StringVar()
Layout_Radius_Entered = ttk.Entry(monty2, width=12, textvariable = Layout_Radius)
Layout_Radius_Entered.grid(column=2, row=6, sticky='W')

# 顺时针偏转角度
Clockwise_Deflection_Angle = tk.StringVar()
Clockwise_Deflection_Angle_Entered = ttk.Entry(monty2, width=12, textvariable = Clockwise_Deflection_Angle)
Clockwise_Deflection_Angle_Entered.grid(column=2, row=7, sticky='W')

# 添加button
action = ttk.Button(monty2, text="计算", width=9, command=Calculate_2)
action.grid(column=3,row=8)
#---------------Tab2控件介绍结束------------------#
#------------------------------------------------------------------------------------------------------------------------------------
#---------------Tab3控件介绍开始------------------#
# We are creating a container tab3 to hold all other widgets
monty3 = ttk.LabelFrame(tab3, text='仅支持使用EB编写的实验程序：')
monty3.grid(column=0, row=0, padx=8, pady=4)

log_file_path = ''

# 定义加载log文件的callback
def click_load_button():

    global log_file_path

    log_fp = filedialog.askopenfilename()

    # 设置显示的路径内容
    find_index = log_fp.count('/') - 3
    count_num = 0
    for i in range(0,len(log_fp)):
        if log_fp[i] == '/':
            count_num = count_num + 1
            if count_num == find_index:
                break
    path_2_show = '...' + log_fp[i:len(log_fp)]
    ttk.Label(monty3, text="             ").grid(column=4, row=0, columnspan=2, sticky='W')
    ttk.Label(monty3, text=path_2_show).grid(column=4, row=0, columnspan=6, sticky='W')

    # 获取文件的绝对路径
    find_index = log_fp.count('/')
    count_num = 0
    for i in range(0,len(log_fp)):
        if log_fp[i] == '/':
            count_num = count_num + 1
            if count_num == find_index:
                break
    log_file_path = log_fp[0:(i+1)]

# 定义转化callback
def click_run_button():
    # 引用全局变量
    global log_file_path

    # 获取输入内容
    node_1 = node_name_1.get()
    node_2 = node_name_2.get()
    node_3 = node_name_3.get()
    node_4 = node_name_4.get()
    node_5 = node_name_5.get()
    message_1 = message_name_1.get()
    message_2 = message_name_2.get()
    message_3 = message_name_3.get()
    message_4 = message_name_4.get()
    message_5 = message_name_5.get()

        # 判断 1-5 个填入框状态
    if (node_1 == '') | (message_1 == ''):
        enable_1 = 0
    else:
        enable_1 = 1

    if (node_2 == '') | (message_2 == ''):
        enable_2 = 0
    else:
        enable_2 = 1

    if (node_3 == '') | (message_3 == ''):
        enable_3 = 0
    else:
        enable_3 = 1

    if (node_4 == '') | (message_4 == ''):  
        enable_4 = 0
    else:   
        enable_4 = 1

    if (node_5 == '') | (message_5 == ''):
        enable_5 = 0
    else:
        enable_5 = 1

    # 打开eb_message.log
    log_file = open((log_file_path + 'eb_messages.log'), 'r')

    # 打开一个txt文件作为输出
    add_file_name = log_file_path + 'msg_add.txt'
    if os.path.exists(add_file_name):
        os.remove(add_file_name)
    file_handle = open(add_file_name, 'a+')

    # main loop

    for line in log_file:
        
        text_line = line.split('    ')
        
        # 计算主试机和被试机之间的时钟时延
        if 'TRACKER_TIME' in text_line[0]:

            space_loc_1 = text_line[0].find(' ')
            trial_time = float(text_line[0][:space_loc_1])

            space_loc_2 = text_line[0][::-1].find(' ')
            tracker_time = float(text_line[0][-space_loc_2:-1])

            sys_delay = tracker_time - trial_time
            print(str(int(sys_delay)))
        # 计算主试机和被试机之间的时钟时延----结束

        this_line_pass = 1

        # 识别message
        # 处理第一条message
        if enable_1:
            if node_1 in text_line[0]:
                if not('(BEGIN)' in text_line[0]):
                    timestap_len = text_line[0].find('.',1) + 4
                    edf_time = sys_delay + float(text_line[0][:timestap_len])
                    msg_text = 'MSG ' + str(int(edf_time)) + ' ' + message_1 + '\n'
                    file_handle.write(msg_text)
                    file_handle.flush()
                    this_line_pass = 0

        # 处理第2条message
        if enable_2 & this_line_pass:
            if node_2 in text_line[0]:
                if not('(BEGIN)' in text_line[0]):
                    timestap_len = text_line[0].find('.',1) + 4
                    edf_time = sys_delay + float(text_line[0][:timestap_len])
                    msg_text = 'MSG ' + str(int(edf_time)) + ' ' + message_2 + '\n'
                    file_handle.write(msg_text)
                    file_handle.flush()
                    this_line_pass = 0

        # 处理第3条message
        if enable_3 & this_line_pass:
            if node_3 in text_line[0]:
                if not('(BEGIN)' in text_line[0]):
                    timestap_len = text_line[0].find('.',1) + 4
                    edf_time = sys_delay + float(text_line[0][:timestap_len])
                    msg_text = 'MSG ' + str(int(edf_time)) + ' ' + message_3 + '\n'
                    file_handle.write(msg_text)
                    file_handle.flush()
                    this_line_pass = 0

        # 处理第4条message
        if enable_4 & this_line_pass:
            if node_4 in text_line[0]:
                if not('(BEGIN)' in text_line[0]):
                    timestap_len = text_line[0].find('.',1) + 4
                    edf_time = sys_delay + float(text_line[0][:timestap_len])
                    msg_text = 'MSG ' + str(int(edf_time)) + ' ' + message_4 + '\n'
                    file_handle.write(msg_text)
                    file_handle.flush()
                    this_line_pass = 0

        # 处理第5条message
        if enable_5 & this_line_pass:
            if node_5 in text_line[0]:
                if not('(BEGIN)' in text_line[0]):
                    timestap_len = text_line[0].find('.',1) + 4
                    edf_time = sys_delay + float(text_line[0][:timestap_len])
                    msg_text = 'MSG ' + str(int(edf_time)) + ' ' + message_5 + '\n'
                    file_handle.write(msg_text)
                    file_handle.flush()

    ttk.Label(monty3, text='已完成').grid(column=8, row=6, sticky='W')

    file_handle.close()

# 创建log文件名显示框
ttk.Label(monty3, text="无项目").grid(column=4, row=0, columnspan=6, sticky='W')

# 创建加载log文件的按钮
load_log_file = ttk.Button(monty3,text="Load file",width=8,command=click_load_button)   
load_log_file.grid(column=0,row=0,columnspan=4)

# 创建Run按钮
Run_savior = ttk.Button(monty3,text="Run",width=6,command=click_run_button)   
Run_savior.grid(column=9,row=6)

# 创建状态指示文本
ttk.Label(monty3, text="未加载").grid(column=8, row=6, sticky='W')

# 创建序号
ttk.Label(monty3, text="1").grid(column=0, row=1, sticky='W')
ttk.Label(monty3, text="2").grid(column=0, row=2, sticky='W')
ttk.Label(monty3, text="3").grid(column=0, row=3, sticky='W')
ttk.Label(monty3, text="4").grid(column=0, row=4, sticky='W')
ttk.Label(monty3, text="5").grid(column=0, row=5, sticky='W')

# 创建内容输入框--------------------------------------------------------------------------
# 第1行
node_name_1 = tk.StringVar()
node_name_1_entry = ttk.Entry(monty3, width=20, textvariable=node_name_1)
node_name_1_entry.grid(column=1, row=1, columnspan=5, sticky='W')

ttk.Label(monty3, text="=>").grid(column=6, row=1, sticky='W')

message_name_1 = tk.StringVar()
message_name_1_entry = ttk.Entry(monty3, width=16, textvariable=message_name_1)
message_name_1_entry.grid(column=7, row=1, columnspan=3, sticky='W')

# 第2行
node_name_2 = tk.StringVar()
node_name_2_entry = ttk.Entry(monty3, width=20, textvariable=node_name_2)
node_name_2_entry.grid(column=1, row=2, columnspan=5, sticky='W')

ttk.Label(monty3, text="=>").grid(column=6, row=2, sticky='W')

message_name_2 = tk.StringVar()
message_name_2_entry = ttk.Entry(monty3, width=16, textvariable=message_name_2)
message_name_2_entry.grid(column=7, row=2, columnspan=3, sticky='W')

# 第3行
node_name_3 = tk.StringVar()
node_name_3_entry = ttk.Entry(monty3, width=20, textvariable=node_name_3)
node_name_3_entry.grid(column=1, row=3, columnspan=5, sticky='W')

ttk.Label(monty3, text="=>").grid(column=6, row=3, sticky='W')

message_name_3 = tk.StringVar()
message_name_3_entry = ttk.Entry(monty3, width=16, textvariable=message_name_3)
message_name_3_entry.grid(column=7, row=3, columnspan=3, sticky='W')

# 第4行
node_name_4 = tk.StringVar()
node_name_4_entry = ttk.Entry(monty3, width=20, textvariable=node_name_4)
node_name_4_entry.grid(column=1, row=4, columnspan=5, sticky='W')

ttk.Label(monty3, text="=>").grid(column=6, row=4, sticky='W')

message_name_4 = tk.StringVar()
message_name_4_entry = ttk.Entry(monty3, width=16, textvariable=message_name_4)
message_name_4_entry.grid(column=7, row=4, columnspan=3, sticky='W')

# 第5行
node_name_5 = tk.StringVar()
node_name_5_entry = ttk.Entry(monty3, width=20, textvariable=node_name_5)
node_name_5_entry.grid(column=1, row=5, columnspan=5, sticky='W')

ttk.Label(monty3, text="=>").grid(column=6, row=5, sticky='W')

message_name_5 = tk.StringVar()
message_name_5_entry = ttk.Entry(monty3, width=16, textvariable=message_name_5)
message_name_5_entry.grid(column=7, row=5, columnspan=3, sticky='W')
# 创建内容输入框结束--------------------------------------------------------------------------

# 一次性控制各控件之间的距离
for child in monty3.winfo_children(): 
    child.grid_configure(padx=3,pady=1)
#---------------Tab3控件介绍结束------------------#

vac.mainloop()