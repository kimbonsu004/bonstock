from random import *
from time import *
from stock import stock_info
from threading import Thread


def set_company_start_price():

    for company in stock_info.keys():

        stock_info[company]["start_price"] = randint(1000, 100000)  # 주식 시초가 , 1000원에서 100000원 사이 가격

        locals()[f"{company}_Th"] = Thread(
            target=set_company_current_price, args=(company,), daemon=True
        )  # 동적변수 , 데몬 쓰레드

        locals()[f"{company}_Th"].start()  # 쓰레드 시작

        stock_info[company]["now_price"] = stock_info[company]["start_price"]


def set_company_current_price(company):

    while True:

        now_price = stock_info[company]["now_price"]

        if 1000 <= now_price < 5000:
            change = 5
        elif 5000 <= now_price < 10000:
            change = 10
        elif 10000 <= now_price < 50000:
            change = 50
        elif 50000 <= now_price < 100000:
            change = 100

        per = randint(1, 100)  # 증감 확률

        if per >= 50:  # 50프로 확률
            now_price += change
        else:
            now_price -= change

        stock_info[company]["now_price"] = now_price

        sleep(5)
