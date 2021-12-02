from client import get_client_stockholding, client_info
from stock import get_stock_list
from company import stock_info
import math


def get_trade_buyable(money, price):
    buyable = math.floor(money / price)
    return buyable


def get_trade_sellable(company):
    return client_info["stock"][company]["amount"]


def trade_buy(company):
    while True:
        try:
            money = client_info["money"]
            price = stock_info[company]["now_price"]
            buyable = get_trade_buyable(money, price)
            if buyable != 0:
                print(f"{company} {price}, {buyable}주 매수 가능")
                print()
                amount = abs(int(input("매수 수량을 입력해주세요. >> ")))
                if buyable >= amount:
                    client_info["stock"][company]["buy_price"] = price
                    client_info["stock"][company]["amount"] += amount
                    client_info["money"] -= price * amount
                    print(f"{company}, {amount}주 매수되었습니다.")
                    break
                else:
                    print("돈이 부족합니다.")
                    continue
            else:
                print("돈이 부족합니다.")
                print()
                break
        except ValueError:
            print("올바른 값을 입력해주세요.")
            print()
            break
        except KeyboardInterrupt:
            break


def trade_sell(company):
    while True:
        try:
            if company in get_client_stockholding():
                price = stock_info[company]["now_price"]
                sellable = get_trade_sellable(company)
                print(f"{company} {price}, {sellable}주 매도 가능")
                print()
                amount = abs(int(input("매도 수량을 입력해주세요. >> ")))
                if sellable >= amount:
                    client_info["stock"][company]["amount"] -= amount
                    client_info["money"] += price * amount
                    print(f"{company}, {amount}주 매도되었습니다.")
                    break
                else:
                    print("보유 주식이 부족합니다.")
                    print()
                    continue
            else:
                print("보유 주식이 부족합니다.")
                print()
                break

        except ValueError:
            print("올바른 값을 입력해주세요.")
            print()
            continue
        except KeyboardInterrupt:
            break


def set_trade():
    while True:
        try:
            print(f"현재 보유 자산은 {client_info['money']:,}원 입니다.")
            print()
            print(get_stock_list())
            print(get_client_stockholding())
            print()
            trade = input("거래하실 종목, 거래 방법을 입력해주세요. >> ").split()

            if trade[0] in get_stock_list():
                if trade[1] == "매수":
                    trade_buy(trade[0])
                    break
                elif trade[1] == "매도":
                    trade_sell(trade[0])
                    break
                else:
                    print("올바른 거래 방법이 아닙니다. [매수 매도]")
                    continue
            else:
                print("존재하지 않는 종목입니다.")
                continue
        except IndexError:
            print("올바른 입력 방법이 아닙니다. [종목] [거래 방법]")
            continue
        except KeyboardInterrupt:
            break
