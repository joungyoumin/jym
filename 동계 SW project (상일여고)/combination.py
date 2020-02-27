from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pygame
import turtle as t
import random



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

    global score 
    score = 0 # 점수 저장
    global playing
    playing = False #현재 게임이 플레이 중인지 확인하는 함수
    te = t.Turtle()
    te.color("red")
    te.speed(150)
    te.up()
    te.goto(0,200)

    ts = t.Turtle()
    ts.shape("circle")
    ts.color("green")
    ts.speed(20)
    ts.up()
    ts.goto(0,-200)


    def turn_right():
        t.setheading(0)
    def turn_up():
        t.setheading(90)
    def turn_left():
        t.setheading(180)
    def turn_down():
        t.setheading(270)

    def start(): #게임을 시작하는 함수
        global playing
        if playing ==False:
            playing =True
            t.clear() #메시지를 지움
            play()

    def play():
        global score 
        global playing 
        t.fd(20) 
        if random.randint(1,5) == 3: #1에서 5까지 임의수를 뽑는건데 임의수=3이면의 가정(20%확률)
            ang = te.towards(t.pos()) #position
            te.setheading(ang)
        speed = score + 25 #점수가 올라가면 빨라짐
        if speed > 115: #속도가 15를 넘지 않게함
            speed = 15
        te.forward(speed)
        if t.distance(te) < 12: #주인공과 거리가 12보다 작으면 게임을 종료함
            text = "Score:" +str(score)
            message("Game Over", text)
            playing = False
            score = 0
            ts.goto(0,-200)
        if t.distance(ts) < 12: #주인공과 거리가 12보다 작으면
            score = score + 1 #점수를 올림
            t.write(score)#점수를 화면에 표시
            star_x = random.randint (-230, 230)
            star_y = random.randint (-230, 230)
            ts.goto(star_x, star_y) #먹이를 옮김
        if playing:
            t.ontimer(play, 100)

    def message(m1,m2): #메세지를 화면에 표시
        t.clear()
        t.goto(0,100)
        t.write(m1, False, "center", ("", 20))
        t.goto(0, -100)
        t.write(m2, False, "center", ("", 15))
        t.home()


    t.title("Turtle Run") #제목
    t.setup(500,500)
    t.bgcolor("orange")
    t.shape("turtle")
    t.speed(0)
    t.up()
    t.color("white")
    t.onkeypress(turn_right, "Right") #방향키 오른쪽 화살표
    t.onkeypress(turn_up, "Up")
    t.onkeypress(turn_left, "Left")
    t.onkeypress(turn_down, "Down")
    t.onkeypress(start, "space") #시작
    t.listen()
    message("Turtle Run", "[space]") #첨가

    t.mainloop()
    

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



































