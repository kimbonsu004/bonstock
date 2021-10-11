from client import *
from PL import *
import company
from trading import *
from threading import Thread
from company import *
import os

os.system("cls")


def service():
    print("{0}님 어서오세요,".format(my_name),end="")
    print(" 원하시는 업무를 선택하여 주세요")
    
    while True:

        service_num=int(input(
"""
[1] : 주식 거래
[2] : 자산 현황
[3] : 실현 손익

>>>  """))

        if service_num==1:
            trade()
        elif service_num==2:
            print("")
            My_asset()
        elif service_num==3:
            print("")
            PLfind()
        else:
            print("해당 서비스가 존재하지 않습니다. 다시 입력해주세요.")
            continue


def My_asset(): # 자산현황 조회 , myAsset 의 mymoney mystock 를 받는다
    print("{0}님의 보유 자산은 {1:,}원 입니다.".format(my_name,my_money))


my_name, my_money, my_stock=client() # client 함수의 리턴값을 받음

print("""

______ __   __  _____  _                 _    
| ___ \\ \ / / /  ___|| |               | |   
| |_/ / \ V /  \ `--. | |_   ___    ___ | | __
|  __/   \ /    `--. \| __| / _ \  / __|| |/ /
| |      | |   /\__/ /| |_ | (_) || (__ |   < 
\_|      \_/   \____/  \__| \___/  \___||_|\_\
                                              
                                              
""")

th=Thread(target=companystock.price)

th.start()

service()

th.join()

