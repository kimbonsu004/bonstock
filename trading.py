from PL import PL
from client import *
from companystock import *


def trade():

    for key in clientData['stock'].keys():
        print(key, end="  ")

    while True:
        try:
            command_stock = input("거래하실 종목을 입력해주세요 >> ").lower()

            if command_stock not in clientData['stock']:
                print("존재하지 않는 종목입니다.")
                continue
            else:
                Comtrade(command_stock)
                break
        except KeyboardInterrupt:
            break


def Comtrade(Company):

    Mymoney = clientData['money']

    command_trading = input("[매수 | 매도] 거래 방법을 입력해주세요 >> ")

    if command_trading == "매수":  # 매수

        buyprice = clientData['stock'][Company]['currentprice']

        clientData['stock'][Company]['buyprice'] = buyprice

        buyable = round(Mymoney/buyprice)-1  # 구매 가능 수량

        print(f"매수 가능 수량은 {buyable} 주 입니다. 현재 금액 {buyprice} 원")

        while True:
            capacity = input("매수 수량을 입력해주세요 >> ")
            if capacity.isdigit() == False:
                print('숫자로만 입력해주세요.')
                continue
            elif capacity == 0:
                print("유효하지 않은 수량입니다.")
                continue
            else:
                capacity = int(capacity)
                break

        if capacity > buyable:  # 매수량 100 ? 가능량 50 , 실패 -> 전량 매수

            Mymoney -= buyprice*buyable
            clientData['stock'][Company]['capacity'] += buyable
            print(f'{buyable:,} 주 매수되었습니다.  현재 보유 금액 : {Mymoney:,} 원')
            clientData['money'] = Mymoney
            print("전량 매수되었습니다.")

        elif capacity <= buyable:  # 매수량 50 ? 가능량 100 , 성공 함수호출
            Mymoney -= buyprice*capacity
            clientData['stock'][Company]['capacity'] += capacity
            print(f'{capacity:,} 주 매수되었습니다.  현재 보유 금액 : {Mymoney:,} 원')
            clientData['money'] = Mymoney

    elif command_trading == "매도":  # 매도

        sellprice = clientData['stock'][Company]['currentprice']
        sellable = clientData['stock'][Company]['capacity']  # 사용자가 보유한 수량이다

        if sellable == 0:  # 보유 주식 수량 확인
            print("보유 주식이 없어 거래가 불가능 합니다.")

        else:
            print(f"매도 가능 수량은 {sellable} 주 입니다. 현재 금액 {sellprice} 원")
            while True:
                capacity = input("매도 수량을 입력해주세요 >> ")
                if capacity.isdigit() == True:
                    capacity = int(capacity)  # 사용자가 판매할 수량이다
                    break
                elif capacity == 0:
                    print("유효하지 않은 수량입니다.")
                    continue
                else:
                    print('숫자로만 입력해주세요.')
                    continue

            if capacity > sellable:  # 매도량 100 ? 가능량 50 , 실패 -> 전량매도
                Mymoney += sellprice*sellable
                clientData['stock'][Company]['capacity'] -= sellable
                print(f'{sellable:,} 주 매도되었습니다. 현재 보유 금액 : {Mymoney:,} 원')
                clientData['money'] = Mymoney
                print("전량 매도되었습니다.")

            elif capacity <= sellable:  # 매도량 50 ? 가능량 100 , 성공 함수호출
                Mymoney += sellprice*capacity
                clientData['stock'][Company]['capacity'] -= capacity
                print(f'{capacity:,} 주 매도되었습니다.  현재 보유 금액 : {Mymoney:,} 원')
                clientData['money'] = Mymoney
