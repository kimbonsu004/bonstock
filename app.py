from client import *
from PL import *
from streamstock import *
from trading import *
from threading import Thread
from companystock import *
import os
import platform

os.system("cls")

def service():
    my_name=clientData['name']
    print("{0}님 어서오세요,".format(my_name),end="")
    print(" 원하시는 업무를 선택하여 주세요")
    
    while True:

        service_num=input(
"""
[1] : 주식 거래
[2] : 실시간 주가
[3] : 자산 현황
[4] : 실현 손익
[5] : 실현 손익 (선택)

>>>  """)

        if service_num.isdigit()==True:
            service_num=int(service_num)
            if service_num==1:
                trade()
            elif service_num==2:
                print()
                stream()
            elif service_num==3:
                print()
                My_asset()
            elif service_num==4:
                print()
                PL()
            elif service_num==5:

                select_stock_able=[]

                for key in clientData['stock'].keys():
                    if clientData['stock'][key]['capacity'] != 0:
                        select_stock_able.append(key)

                print(select_stock_able)

                while True:
                    select_stock = input("확인하실 종목을 입력해주세요 >> ").lower()
                    if select_stock not in clientData['stock']:
                        print("존재하지 않는 종목입니다.")
                        continue
                    elif select_stock not in select_stock_able:
                        print("보유하지 않은 종목입니다")
                        continue
                    else:
                        print("메인으로 돌아가시려면 ctrl + c \n")
                        PLone(select_stock)
                        break

            elif service_num==99:
                if platform.system()=='Windows':
                    os.system('cls')
                else:
                    os.system('clear')
            else:
                print("해당 서비스가 존재하지 않습니다.")
                continue
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue


def My_asset(): # 자산현황 조회 , myAsset 의 mymoney mystock 를 받는다
    my_name=clientData['name']
    my_money=clientData['money']
    print("{0}님의 보유 자산은 {1:,}원 입니다.".format(my_name,my_money))

print("""

______ __   __  _____  _                 _    
| ___ \\ \ / / /  ___|| |               | |   
| |_/ / \ V /  \ `--. | |_   ___    ___ | | __
|  __/   \ /    `--. \| __| / _ \  / __|| |/ /
| |      | |   /\__/ /| |_ | (_) || (__ |   < 
\_|      \_/   \____/  \__| \___/  \___||_|\_\
                                              
                                              
Python mock stock trading program by "kimbonsu004"

Developer Github : https://github.com/kimbonsu004

Thank you for using my program  。˚˚✧₊ ⁎⁺˳✧༚ ♡ミ


if you want 'clear' , service num is '99' 

""")

th=Thread(target=price,daemon=True)

th.start()

client()

service()

