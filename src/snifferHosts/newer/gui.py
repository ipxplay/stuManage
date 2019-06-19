import tkinter
from tkinter import messagebox
from time import *
import queue
# first: system
# second:third
# third:mine
import pandas


from snifferHosts.newer import sniffer_thread


def sayHello(msg="wxit"):
    sleep(20)
    messagebox.showinfo("hello",msg)
    

windows = tkinter.Tk()
t1 = tkinter.Text(windows)
q = queue.Queue()
q.put(t1)
t1.pack()
bt = tkinter.Button(windows,text="SUBMIT",command=lambda:sniffer_thread(t1)).pack()
windows.mainloop()
