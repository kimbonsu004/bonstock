from company import *

mymoney=100000
abc_mystock=0

abc.price()

# command=input("원하시는 거래를 입력해주세요 >>> ")

# if command=="매수":

#     buy=int(input("매수량을 입력해주세요 >>> "))

#     if abc*buy > mymoney:
#         print("잔고가 부족합니다")

#     elif abc*buy < mymoney:
#         print("{} 주 매수되었습니다".format(buy))
#         abc_mystock+=buy
#         mymoney-=abc*buy

# elif command=="매도":

#     sell = int(input("매도량을 입력해주세요 >>>"))

#     if sell>abc_mystock:
#         print("보유 주식이 부족합니다")

#     elif sell<abc_mystock:
#         print("{} 주 매도되었습니다".format(sell))
#         abc_mystock-=sell
#         mymoney+=abc*sell

# elif command=="대기":
#     pass

