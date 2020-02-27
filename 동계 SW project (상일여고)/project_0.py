# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:57:57 2020

@author: Joung YouMin
"""
from tkinter import *
import numpy as np

window = Tk()

window.title("My Calculator")

display = Entry(window, width=20,bd=3, insertborderwidth=2,insertwidth=2,fg="white",bg="pink", font='helvetica 16 italic')
display.grid(row=0, column=0, columnspan=5)

button_list = [
'7',  '8',  '9',  '/',  'C',
'4',  '5',  '6',  '*',  '<-',
'1',  '2',  '3',  '-',  'bin',
'0',  '.',  '=',  '+',  'ln' ]

def click(key):
    
    
    if key == "=":
        result = eval(display.get())
        s = str(result)
        display.delete(0, END)
        display.insert(0,s)
    elif key == "<-" :
        a = list(display.get())
        display.delete(len(a)-1,len(a))
    elif key == "C" :
        display.delete(0, END)
    elif key == "bin" :
        result = int(display.get())
        s = bin(result)[2:]
        s = str(s)
        display.delete(0, END)
        display.insert(0,s)
    elif key == "ln" :
        s = np.log(float(display.get()))
        display.delete(0, END)
        display.insert(0,s)
    else:
        display.insert(END, key)
        

row_index = 1
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width=5, height=2,font='helvetica 15 italic',	
		command=process).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0

window.mainloop()