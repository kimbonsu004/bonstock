from PL import PL
from client import *
from company import *

def Comtrade(Company):

    Mymoney = clientData['money']

    command_trading = input("[매수 | 매도] 거래 방법을 입력해주세요 >> ")
            
    if command_trading == "매수":
        
        buyprice=clientData['stock'][Company]['currentprice']

        clientData['stock'][Company]['buyprice'] = buyprice

        buyable = round(Mymoney/buyprice) # 구매 가능 수량

        print("매수 가능 수량은 {0:,} 주 입니다".format(buyable))

        capacity=int(input("매수 수량을 입력해주세요 >> "))

        if capacity>buyable:  # 매수량 100 ? 가능량 50 , 실패
            print("돈이 부족합니다 !")

        elif capacity<=buyable: # 매수량 50 ? 가능량 100 , 성공 함수호출
            Mymoney=-buyprice*capacity
            clientData['stock'][Company]['capacity']=+capacity
            print(f'{capacity} 주 매수되었습니다.  보유 금액 : {Mymoney:,} 원')


def trade():

    for key in clientData['stock'].keys():
        print(key,end="  ")

    print()

    command_stock = input("거래하실 종목을 입력해주세요 >> ").lower()

    Comtrade(command_stock)