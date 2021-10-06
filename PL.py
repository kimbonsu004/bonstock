from company import *
from client import *

def PL(beginprice,capacity):

    clientData['stock']['Apple']['price']  = beginprice # apple_begining #client 딕셔너리와 연동

    apple_beginning = clientData['stock']['Apple']['price'] # 딕셔너리 값 할당

    Myapple_beginning = apple_beginning * capacity  # 변수에 가격* 보유량 할당 , 총금액

    clientData['stock']['Apple']['capacity']  = capacity #  해당 딕셔너리에 값 대입, 변수에 할당

    while True:

        Myapple_current = Apple.current_price(apple_beginning) * capacity

        if Myapple_beginning>Myapple_current: # 손해일 경우
            lost=round(((Myapple_current/Myapple_beginning*100) - 100),3)
            print("\rApple 매수액 : {0:,}   현재가 : {1:,}  수익률 : {2}% ".format(Myapple_beginning, Myapple_current, lost),end="")

        elif Myapple_beginning<Myapple_current: # 이익일 경우
            profit=round(((Myapple_current/Myapple_beginning*100) - 100),3)
            print("\rApple 매수액 : {0:,}   현재가 : {1:,}  수익률 : + {2}% ".format(Myapple_beginning, Myapple_current, profit),end="")