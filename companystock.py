from random import *
from time import *
from client import clientData

def price(): 

    for key in clientData['stock'].keys():

        beginnig_pirce=0

        beginnig_pirce=randint(1000,10000) # 주식 시초가 , 1000원에서 10000원 사이 가격

        clientData['stock'][key]['currentprice'] = beginnig_pirce

        #print(f'{key} 의 값은 {beginnig_pirce}')

    current_price()

def current_price(): # 백그라운드에서 계속 변화를 줄것임

    while True:

        for key in clientData['stock'].keys():

            company_beginning=clientData['stock'][key]['currentprice']

            #print('{0}의 값은 {1}'.format(key,clientData['stock'][key]['currentprice']))

            change=round(company_beginning*random()*00.1) # 증감량 10% 이내 증감

            per=randint(1,100) # 증감 확률

            if per>=50:      # 50프로 확률
                Company_current=company_beginning+change
            else:
                Company_current=company_beginning-change

            clientData['stock'][key]['currentprice']=Company_current

            #print(f"{key} 값은 {clientData['stock'][key]['currentprice']}")

            sleep(3)

#price()