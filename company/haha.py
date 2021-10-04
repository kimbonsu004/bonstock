from random import *
from time import *

def price():

    haha_price=randint(1000,10000) # 주식 현재가 , 1000원에서 10000원 사이 가격

    change=haha_price/randint(50,500) # 증감량 , 10& 이내에서 등락

    per=randint(1,100) # 증감 확률

    if per>=40:      # 60프로 확률
        haha_price+=change
    else:
        haha_price-=change
    
    return haha_price



