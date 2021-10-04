from client import *

my_name, my_money, my_stock=client() # client 함수의 리턴값을 받음

def service():
    print(" 원하시는 업무를 선택하여 주세요")
    service_num=int(input(
"""
[1] : 주식 거래
[2] : 자산 현황
[3] : 실현 손익

>>>  """))

    if service_num==1:
        pass
    elif service_num==2:
        My_asset()
    elif service_num==3:
        pass


def My_name(): # 환영인사, myName 의 Myname 를 받는다.
    print("\r{0}님 어서오세요,".format(my_name),end="")


def My_asset(): # 자산현황 조회 , myAsset 의 mymoney mystock 를 받는다
    print("\r{0}님의 보유 자산은 {1}원 입니다.,".format(my_name,my_money),end="")



print("""

______ __   __  _____  _                 _    
| ___ \\ \ / / /  ___|| |               | |   
| |_/ / \ V /  \ `--. | |_   ___    ___ | | __
|  __/   \ /    `--. \| __| / _ \  / __|| |/ /
| |      | |   /\__/ /| |_ | (_) || (__ |   < 
\_|      \_/   \____/  \__| \___/  \___||_|\_\
                                              
                                              
""")

My_name()

service()
