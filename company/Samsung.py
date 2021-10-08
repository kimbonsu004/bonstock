from random import *
from time import *
from client import *

def price(): # 백그라운드에서 계속 변화를 줄것임
 
    Samsung_beginning=randint(1000,10000) # 주식 시초가 , 1000원에서 10000원 사이 가격

    current_price(Samsung_beginning) # 시초가를 넘겨 주가 등락 시작

    return Samsung_beginning

def current_price(Samsung_beginning):

    while True:

        change=round(Samsung_beginning*random()*00.1) # 증감량 10% 이내 증감

        per=randint(1,100) # 증감 확률

        if per>=50:      # 60프로 확률
            Samsung_curent=Samsung_beginning+change
        else:
            Samsung_curent=Samsung_beginning-change

        clientData['stock']['samsung']['currentprice']=Samsung_curent 

        sleep(5)