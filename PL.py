from client import *
from companystock import *


class Colors:
    RED = '\033[31m'
    BLUE = '\033[34m'
    RESET = '\033[0m'


def PL():

    for Company in clientData['stock'].keys():

        buyprice = clientData['stock'][Company]['buyprice']  # 구매 금액 딕셔너리 참조

        capacity = clientData['stock'][Company]['capacity']   # 구매 수량 딕셔너리 참조

        MyCompany_buying = buyprice * capacity  # 변수에 구매 가격 * 보유량 할당 , 총 매수 금액

        # 변화중인 현재가를 가져옴
        MyCompany_current = clientData['stock'][Company]['currentprice'] * capacity

        if capacity > 0:

            if buyprice != 0:

                if MyCompany_buying > MyCompany_current:  # 손해일 경우

                    lost = round(
                        ((MyCompany_current/MyCompany_buying*100) - 100), 3)

                    print("\r\n"+f"{Company}  매수액 : {MyCompany_buying:,}   현재가 : {MyCompany_current:,}" +
                          "  수익률 : " + Colors.BLUE + f" {lost} %" + Colors.RESET, end="  ")

                elif MyCompany_buying < MyCompany_current:  # 이익일 경우

                    profit = round(
                        ((MyCompany_current/MyCompany_buying*100) - 100), 3)

                    print("\r\n"+f"{Company}  매수액 : {MyCompany_buying:,}   현재가 : {MyCompany_current:,}" +
                          "  수익률 : " + Colors.RED + f" + {profit} %" + Colors.RESET, end="   ")

                print()

            else:
                pass

        else:
            pass


def PLone(Company):

    while True:

        try:

            # 구매 금액 딕셔너리 참조
            buyprice = clientData['stock'][Company]['buyprice']

            # 구매 수량 딕셔너리 참조
            capacity = clientData['stock'][Company]['capacity']

            MyCompany_buying = buyprice * capacity  # 변수에 구매 가격 * 보유량 할당 , 총 매수 금액

            # 변화중인 현재가를 가져옴
            MyCompany_current = clientData['stock'][Company]['currentprice'] * capacity

            if capacity > 0:

                if buyprice != 0:

                    if MyCompany_buying > MyCompany_current:  # 손해일 경우

                        lost = round(
                            ((MyCompany_current/MyCompany_buying*100) - 100), 3)

                        print("\r"+f"{Company}  매수액 : {MyCompany_buying:,}   현재가 : {MyCompany_current:,}" +
                              "  수익률 : " + Colors.BLUE + f" {lost} %" + Colors.RESET, end="  ")

                    elif MyCompany_buying < MyCompany_current:  # 이익일 경우

                        profit = round(
                            ((MyCompany_current/MyCompany_buying*100) - 100), 3)

                        print("\r"+f"{Company}  매수액 : {MyCompany_buying:,}   현재가 : {MyCompany_current:,}" +
                              "  수익률 : " + Colors.RED + f" + {profit} %" + Colors.RESET, end="   ")

                else:
                    pass

            else:
                pass

        except KeyboardInterrupt:
            break
