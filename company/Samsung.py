from random import *
from time import *

def price():

    abc_price=randint(1000,10000) # 주식 현재가 , 1000원에서 10000원 사이 가격

    while True:

        change=round(abc_price/randint(50,500)) # 증감량 , 10& 이내에서 등락

        per=randint(1,100) # 증감 확률

        if per>=40:      # 60프로 확률
            abc_price+=change
        else:
            abc_price-=change
        
        print("\r 현재 가격 : {}".format(abc_price),end="")

        sleep(10)



