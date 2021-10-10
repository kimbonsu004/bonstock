from random import *
from time import *
from client import *
import company

def price(): # 백그라운드에서 계속 변화를 줄것임

    for key in clientData['stock'].keys():

        key_beginning=randint(1000,10000) # 주식 시초가 , 1000원에서 10000원 사이 가격

        clientData['stock'][key]['currentprice'] = key_beginning

def current_price():

    while True:

        for key in clientData['stock'].keys():

            company_beginning=clientData['stock'][key]['currentprice']

            change=round(company_beginning*random()*00.1) # 증감량 10% 이내 증감

            per=randint(1,100) # 증감 확률

            if per>=50:      # 60프로 확률
                Company_curent=company_beginning+change
            else:
                Company_curent=company_beginning-change

            clientData['stock'][key]['currentprice']=Company_curent 

        sleep(5)