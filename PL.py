from company import *
from client import *

class Colors: 
    RED = '\033[31m' 
    BLUE = '\033[34m' 
    RESET = '\033[0m'

def PL(Company):
    
    while True:

        buyprice = clientData['stock'][Company]['buyprice'] # 구매 금액 딕셔너리 참조

        capacity = clientData['stock'][Company]['capacity']   # 구매 수량 딕셔너리 참조

        MyCompany_buying = buyprice * capacity  # 변수에 구매 가격 * 보유량 할당 , 총 매수 금액

        MyCompany_current = clientData['stock'][Company]['currentprice'] * capacity #변화중인 현재가를 가져옴

        if MyCompany_buying>MyCompany_current: # 손해일 경우
            lost=round(((MyCompany_current/MyCompany_buying*100) - 100),3)
            print("\r{0} 매수액 : {1:,}   현재가 : {2:,}  수익률 : {3}% ".format(Company,MyCompany_buying, MyCompany_current, lost),end="")

        elif MyCompany_buying<MyCompany_current: # 이익일 경우
            profit=round(((MyCompany_current/MyCompany_buying*100) - 100),3)
            print("\r{0} 매수액 : {1:,}   현재가 : {2:,}  수익률 : + {3}% ".format(Company,MyCompany_buying, MyCompany_current, profit),end="")