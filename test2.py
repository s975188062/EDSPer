from tkinter import *
import tkinter 
import time
import threading

event = threading.Event()
def start():
    event.set()
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True)
    t1.start()
def stop():
    event.clear
    print('暂停')
def conti():
    event.set
    print('继续')
def thread():
    while True:
        print('运行中')
        time.sleep(1)
        event.wait()
window = Tk()
window.title('测试')
b1=Button(window,text='start',command=start)
b1.pack()
b2=Button(window,text='stop',command=stop)
b2.pack()
b3=Button(window,text='conti',command=conti)
b3.pack()
mainloop()