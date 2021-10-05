from random import *
from time import *

def price():

    Apple_beginning=randint(1000,10000) # 주식 시초가 , 1000원에서 10000원 사이 가격

    return Apple_beginning

def current_price(Apple_beginning):
    
    Apple_curent=0

    while True:

        sleep(3)

        change=round(Apple_beginning*random()*0.1) # 증감량 10% 이내 증감

        per=randint(1,100) # 증감 확률

        if per>=40:      # 60프로 확률
            Apple_curent=Apple_beginning+change
        else:
            Apple_curent=Apple_beginning-change

        return Apple_curent



