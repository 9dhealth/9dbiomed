#!/usr/bin/env python
# coding: utf-8

# In[21]:


# 将原来的1.x版本的excel to 列表修改为2.0版本的csv to 字典，只需导入csv模块，更简洁大方，可读性也提高，除此之外，CSV比exce更适合树立大量数据
import csv
from copy import deepcopy
from tkinter import *
import tkinter.filedialog
from tkinter.messagebox import showinfo

filename = ""
filepath = ""


def select_file():
    global filename
    filename = tkinter.filedialog.askopenfilename()
    if len(filename) != 0:
        var1.set(filename)
    else:
        var1.set("您没有选择任何文件")
    return filename


def save_directory():
    global filepath
    filepath = tkinter.filedialog.askdirectory()
    if len(filepath) != 0:
        var4.set(filepath)
    else:
        var4.set("您没有选择文件保存位置")
    
    return filepath


def not_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return False
    return True

def csv2dict(filepath):
    with open(filepath, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        fieldnames = next(csv_reader)
        csv_reader = csv.DictReader(f, fieldnames=fieldnames,delimiter=',')
        data = []
        for row in csv_reader:
            new_dict={}
            for k,v in row.items():
                # 统一RSID以及去除空格
                new_dict[k.strip().upper()]=v.strip().upper()
            data.append(new_dict)
    return data 

def double_seq(seq):
    num = len(seq)
    for i in range(0,num):
        newseq = seq[i]
        for key,value in newseq.items():
            if not_Chinese(key):
                if len(value) == 1:
                    value = value*2
                    newseq[key] = value
    return seq

def datalist2csv(lists, out_file):
    with open(out_file, 'w',newline='') as f:
        w = csv.writer(f)
        fieldnames=lists[0].keys() 
        w.writerow(fieldnames)
        for row in lists:
            w.writerow(row.values())


def file_run(): 
    global finaldata
    if len(filename) !=0 and len(filepath)!=0:
        data = csv2dict(filename)
        result = double_seq(data)
        get_data = datalist2csv(result, filepath + "/newdata.csv")
        tkinter.messagebox.showinfo('提示','DNA序列标准化工具完毕')
    else:
        tkinter.messagebox.showwarning('警告','请确认时是否选择了需要分析的文件或者保存的文件位置！')      
            


root = Tk()
root.geometry('500x200')
# 设置窗口是否可以变化长宽
root.resizable(width=False, height=False)
root.title("基因序列标准化工具 2.1")


frame1 = Frame(root)
frame1.pack(padx=10,pady=10)
frame4 = Frame(root)
frame4.pack(padx=10,pady=10)
frame5 = Frame(root)
frame5.pack(padx=60,pady=20)

global var1,var4
var1 = StringVar()
ent1 = Entry(frame1,width =50,textvariable=var1)
ent1.pack(fill=X,side=LEFT,padx=10)
var1.set("")
btn1 = Button(frame1,width =25,text='选择文件',font=("雅黑",14),command = select_file)
btn1.pack(fill=X,padx=10)

var4 = StringVar()
ent4 = Entry(frame4,width =50,textvariable=var4)
ent4.pack(fill=X,side=LEFT,padx=10)
var4.set("")
btn4 = Button(frame4,width =25,text='保存位置',font=("雅黑",14),command = save_directory)
btn4.pack(fill=X,padx=10)

etb = Button(frame5,width =10,text='运行',bg='Teal',fg='White',font=("雅黑",14),activeforeground = 'SkyBlue',command = file_run)
etb.pack(fill=X,padx=10)


menubar = Menu(root)
submenu= Menu(menubar,tearoff=0)
submenu.add_command(label="版本信息：V2.1-TAOHAI")
submenu.add_separator()
submenu.add_command(label="退出",command=root.quit)
menubar.add_cascade(label="菜单",menu=submenu)
root.config(menu=menubar)



root.mainloop()


# In[ ]:





# In[ ]:




