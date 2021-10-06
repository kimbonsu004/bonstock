from PL import PL
from client import *
from company import *
from company.Apple import price

def trade():

    Mymoney = clientData['money']

    for key in clientData['stock'].keys():
        print(key,end="  ")

    print()

    command_stock = input("거래하실 종목을 입력해주세요 >> ")

    if command_stock == "Apple":
        command_trading = input("[매수 | 매도] 거래 방법을 입력해주세요 >> ")
            
        if command_trading == "매수":
            
            buyprice=price()

            buyable = round(Mymoney/price())

            print("구매 가능량은 {} 주 입니다".format(buyable))

            capacity=int(input("매수 수량을 입력해주세요 >> "))

            if capacity>buyable:  # 매수량 100 ? 가능량 50 , 실패
                print("돈이 부족합니다 !")

            elif capacity<=buyable: # 매수량 50 ? 가능량 100 , 성공 함수호출
                PL(buyprice,capacity)
                # 매수 거래 호출

        elif command_trading == "매도":
            capacity=int(input("매도 수량을 입력해주세요 >> "))
            # 매도 거래 호출