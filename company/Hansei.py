from random import *
from time import *
from client import *

def price(): # 백그라운드에서 계속 변화를 줄것임
 
    Hansei_beginning=randint(1000,10000) # 주식 시초가 , 1000원에서 10000원 사이 가격

    current_price(Hansei_beginning) # 시초가를 넘겨 주가 등락 시작

    return Hansei_beginning

def current_price(Hansei_beginning):

    while True:

        change=round(Hansei_beginning*random()*00.1) # 증감량 10% 이내 증감

        per=randint(1,100) # 증감 확률

        if per>=50:      # 60프로 확률
            Hansei_curent=Hansei_beginning+change
        else:
            Hansei_curent=Hansei_beginning-change

        clientData['stock']['hansei']['currentprice']=Hansei_curent 

        sleep(5)