from random import *
from time import *

def price():

    abc_price=3500

    abc_price_current=round(abc_price,0)  # 주식 현재가

    change=round(random(),2)*500 # 증감

    per=randint(1,100)

    if per>=40:      # 60프로 확률
        abc_price_current+=change
    else:
        abc_price_current-=change
    
    return abc_price_current



