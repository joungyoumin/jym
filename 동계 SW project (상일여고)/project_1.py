# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:01:59 2020

@author: Joung YouMin
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


inf = {}


def login_click1():
    
    messagebox.showinfo(title="알림", message="존재하지 않는 아이디 입니다. 회원가입을 해주세요.")
    e1.delete(0, END)
    e2.delete(0, END)
    
def login_click2():
    
    a = inf[e1.get()]
    messagebox.showinfo(title="알림", message=a["age"]+" "+a["gender"]+" "+a["name"]+" 님 환영합니다.")
    e1.delete(0, END)
    e2.delete(0, END)

def login_click3():
    messagebox.showinfo(title="알림", message="비밀번호가 일치하지 않습니다.")
    e2.delete(0, END)    

def login():
    
    
    if e1.get() not in inf.keys():
        login_click1()
    
    elif e1.get() in inf.keys():
        
        a = inf[e1.get()]
        if a["Password"] == e2.get():
            login_click2()
        else :
            login_click3()

def entry():
    
    window1 = Tk()
    window1.title("회원가입")
    
    strs = StringVar()
    strs2 = StringVar()

    l1 = Label(window1 , text="회원 정보를 입력 및 선택 하시오.", font="helvetica 10")
    l1.grid(row=0, column=1)
    l2 = Label(window1, text="ID")
    l2.grid(row=1, column=0)
    l3 = Label(window1, text="Password")
    l3.grid(row=2, column=0)
    l4 = Label(window1, text="name")
    l4.grid(row=3, column=0)
    l5 = Label(window1, text="age")
    l5.grid(row=4, column=0)
    l6 = Label(window1, text="gender")
    l6.grid(row=5, column=0)
    
    e1 = Entry(window1, bg="white", fg="black")
    e1.grid(row=1, column=1,columnspan=3)
    e2 = Entry(window1, bg="white", fg="black")
    e2.grid(row=2, column=1,columnspan=3)
    e3 = Entry(window1, bg="white", fg="black")
    e3.grid(row=3, column=1,columnspan=3)
    
    com1 = ttk.Combobox(window1, textvariable=strs, width = 18)
    com1['value'] = ('나이를 선택하시오.','10대','20대','30대','40대')
    com1.current(0)
    com1.grid(row=4, column=1,columnspan=3)
    com2 = ttk.Combobox(window1, textvariable=strs2, width = 18)
    com2['value'] = ('성별을 선택하시오.','남성','여성')
    com2.current(0)
    com2.grid(row=5, column=1,columnspan=3)
    
    def entry_click():
    
        ID = e1.get()
        Password = e2.get()
        name = e3.get()
        age = com1.get()
        gender = com2.get()
    
        information = {'Password':Password,'name':name,'age':age,'gender':gender}
    
        inf[ID] = information
    
        print(inf)
        
        messagebox.showinfo(title="회원가입 성공", message="회원가입이 완료되었습니다.")
        com1.current(0)
        com2.current(0)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        
    b1 = Button(window1, text="입력완료",command=entry_click)
    b1.grid(row=6, column=1)
   
    window1.mainloop()
     
def find():
    
    window2 = Tk()
    window2.title("비밀번호 찾기")
    
    l1 = Label(window2 , text="ID를 입력하세요 :")
    l1.grid(row=0, column=0)
    e1 = Entry(window2, bg="pink", fg="white")
    e1.grid(row=0, column=1,columnspan=3)
    
    def find_click():
        
        if e1.get() in inf.keys():
            a = inf[e1.get()]
            messagebox.showinfo(title="비밀번호 알림", message=a["Password"])
            e1.delete(0, END)
            
        else :
            login_click1()
            e1.delete(0, END)
    
    b1 = Button(window2, text="확인",command=find_click)
    b1.grid(row=2, column=1)
    
    window2.mainloop()
    
    
window  = Tk()

l1 = Label(window , text="ID")
l2 = Label(window, text="Password")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window, bg="skyblue", fg="black")
e2 = Entry(window, bg="skyblue", fg="black")
e1.grid(row=0, column=1,columnspan=3)
e2.grid(row=1, column=1,columnspan=3)

b1 = Button(window, text="로그인",command=login)
b2 = Button(window, text="회원가입",command=entry)
b3 = Button(window, text="Password 찾기",command=find)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=3)

window.mainloop()
