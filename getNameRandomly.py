#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
import random
import xlrd
import tkinter as tk 
import tkinter.messagebox

data = []
get_number = 0
del_list_value = False
data_copy = []

# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('随机抽签程序')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('300x300')  # 这里的乘是小x

message_corebox = tk.Label(window, text="", bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
message_corebox.pack()

def readData():
    global data, data_copy
    workBook = xlrd.open_workbook("data.xlsx")
    sheet_content = workBook.sheet_by_index(0)
    data = sheet_content.col_values(0)
    data_copy = data[:]
    message_corebox.config(text="已获取{}名学生信息".format(str(len(data))))

def setStudentsNumber(value):
    global get_number
    get_number = int(value)
    message_corebox.config(text="已设置一次性抽取{}名学生".format(str(value)))

def del_list():
    global del_list_value
    if del_it_in_list_value.get() == 1:
        del_list_value = True
        message_corebox.config(text="已设置禁止重复抽取")
    else:
        del_list_value = False
        message_corebox.config(text="已设置允许重复抽取")

def get_the_name():
    global data, get_number, del_list_value, data_copy
    
    try:
        if del_list_value:
            name_list = []
            for _ in range(int(get_number)):
                name = random.choice(data_copy)
                name_list.append(name)
                data_copy.remove(name)
        else:
            name_list = []
            for _ in range(int(get_number)):
                name = random.choice(data)
                name_list.append(name) 
    except IndexError:
        if name_list != []:
            message_for_string = " ".join(name_list)
            tkinter.messagebox.showinfo(title='提示！', message="剩余学生："+message_for_string) 
            tkinter.messagebox.showinfo(title='提示！', message="全部学生已抽取完成！如果要重新开始，请点击重设抽签！")
        else:
            tkinter.messagebox.showinfo(title='提示！', message="全部学生已抽取完成！如果要重新开始，请点击重设抽签！") 
    else:
        tkinter.messagebox.showinfo(title='抽取结果', message=name_list)  
    
def resets():
    global data_copy
    data_copy = data[:]
    tkinter.messagebox.showinfo(title='提示！', message="抽签重设完成！") 

# 第5步，在窗口界面设置放置Button按键
read_but = tk.Button(window, text='读取学生信息', font=('Arial', 12), width=10, height=1, command=readData)
read_but.pack()

# 第5步，创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为1，触发调用print_selection函数
number = tk.Scale(window, label='选择一次性抽取学生的人数', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=setStudentsNumber)
number.pack()

del_it_in_list_value = tk.IntVar() 
del_it_in_list = tk.Checkbutton(window, text='禁止重复抽取',variable=del_it_in_list_value, onvalue=1, offvalue=0, command=del_list)    # 传值原理类似于radiobutton部件
del_it_in_list.pack()

# 第5步，在窗口界面设置放置Button按键
getName = tk.Button(window, text='开始抽签！', font=('Arial', 12), width=10, height=1, command=get_the_name)
getName.pack()

# 第5步，在窗口界面设置放置Button按键
reset = tk.Button(window, text='重设抽签', font=('Arial', 12), width=10, height=1, command=resets)
reset.pack()


window.mainloop()