#!/usr/bin/python3

import threading
import time
#from tkinter.constants import PAGES, SEL_FIRST

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            print_time(self.name, self.counter, 1)
    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞
    def cont(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞
    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False    

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)

# 开启新线程
thread1.start()
time.sleep(2)
print ('pause')
thread1.pause()
time.sleep(2)
print ('go again')
thread1.cont()
thread1.stop()