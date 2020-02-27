# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:40:48 2020

@author: Joung YouMin
"""

import time

def exchange(money):
   
    bending = {'생수':[500,"1개"], '오렌지주스':[2000,"6개"], '콜라': [1500,"3개"]}
    menu = list(bending.keys())
    price = list(bending.values())
   

    while(1) :       
        money = int(money)
        print("돈이 들어왔습니다")
        time.sleep(1)
        print(bending)
        goods = input("상품을 선택하세요 : ")
        goods = int(goods)
        time.sleep(1)
       

        if goods == 1 :
            if money >= 500:
               
                for i in range(1):
               
                    print(menu[i],"을 드립니다")
                    a = price[i]
                    b = a.pop(i+1)
                    c = int(b[:1])
                    c = c-1
                    a.append(str(c)+b[1:2])
                    money = money - a[i]
                    time.sleep(1)
                    print("거스름돈: ", money)
                    time.sleep(1)
                    print(bending)
                    
                    if c == 0:
                        print(menu[i],"은 품절입니다. 다른 상품을 고르세요.")
                        exchange(money)
            else:

                print("돈이 부족합니다.")
                time.sleep(1)
                print("거스름돈: ", money)
                
                
               
               
        elif goods == 2 :
            if money >= 2000:
               
                for i in range(1):
               
                    print(menu[i+1],"을 드립니다")
                    a = price[i+1]
                    z = money - a[i]
                    time.sleep(1)
                    print("거스름돈: ", z)
                    time.sleep(1)
       
                   
            else:

                print("돈이 부족합니다.")
                time.sleep(1)
                print("거스름돈: ", money)
               
        elif goods == 3 :
            if money >= 1500:
               
                for i in range(1):
               
                    print(menu[i+2],"을 드립니다")
                    a = price[i+2]
                    z = money - a[i]
                    time.sleep(1)
                    print("거스름돈: ", z)
                    time.sleep(1)
         
            else:

                print("돈이 부족합니다.")
                time.sleep(1)
                print("거스름돈: ", money)
           
       
        return 0
   
   
   
   

money = input("금액을 넣으세요: ")
exchange(money)