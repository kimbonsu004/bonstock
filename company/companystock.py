from random import *
from time import *
from client import *
import company

def price(): 

    for key in clientData['stock'].keys():

        locals()[f'{key}_beginning']=randint(1000,10000) # 주식 시초가 , 1000원에서 10000원 사이 가격

        clientData['stock'][key]['currentprice'] = locals()[f'{key}_beginning']

    current_price()

def current_price(): # 백그라운드에서 계속 변화를 줄것임

    while True:

        for key in clientData['stock'].keys():

            company_beginning=clientData['stock'][key]['currentprice']

            change=round(company_beginning*random()*00.1) # 증감량 10% 이내 증감

            per=randint(1,100) # 증감 확률

            if per>=50:      # 50프로 확률
                Company_current=company_beginning+change
            else:
                Company_current=company_beginning-change

            clientData['stock'][key]['currentprice']=Company_current