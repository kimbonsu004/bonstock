from stock import stock_info

client_info = {
    "name": "",
    "money": 0,
    "first_check": 0,
    "stock": {
        "apple": {"buy_price": 0, "amount": 0, "earning_rate": 0},
        "hansei": {"buy_price": 0, "amount": 0, "earning_rate": 0},
        "samsung": {"buy_price": 0, "amount": 0, "earning_rate": 0},
        "tessla": {"buy_price": 0, "amount": 0, "earning_rate": 0},
        "theori": {"buy_price": 0, "amount": 0, "earning_rate": 0},
    },
}


class Colors:
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"


def check_client_nulldata():
    if client_info["name"] == "":
        set_client_name()

    if client_info["first_check"] == 0:
        if client_info["money"] == 0:
            set_client_money()
            client_info["first_check"] = 1
    elif client_info["first_check"] == 1:
        print("초기 투자 금액을 설정하신 이력이 있습니다")


def set_client_name():
    client_info["name"] = input("고객님의 성함을 입력해주세요 > > ")


def set_client_money():
    while True:
        try:
            client_info["money"] = abs(int(input("고객님의 투자 금액을 입력해주세요 > > ")))
            break
        except ValueError:
            print("올바르지 않은 값입니다. 정수를 입력해주세요.")
            continue


def show_client_info():
    print(f"{client_info['name']}님의 현재 자산은 {client_info['money']:,} 원 입니다.")


def get_client_stockholding():
    stock_holding = {
        company: client_info["stock"][company]["amount"]
        for company in client_info["stock"].keys()
        if client_info["stock"][company]["amount"] != 0
    }
    if len(stock_holding) == 0:
        return "보유하신 주식이 없습니다."
    else:
        return stock_holding


def show_client_earninginfo():
    for company in client_info["stock"].keys():
        if client_info["stock"][company]["amount"] != 0:
            client_info["stock"][company]["earning_rate"] = round(
                stock_info[company]["now_price"] / client_info["stock"][company]["buy_price"] * 100
                - 100,
                2,
            )
            if client_info["stock"][company]["earning_rate"] > 0:
                print(
                    "\n"
                    f"{company}".ljust(10)
                    + f"매수 : {client_info['stock'][company]['buy_price']:,} ({client_info['stock'][company]['amount']:,}주),  현재가 : {stock_info[company]['now_price']:,} ".ljust(
                        10
                    )
                    + Colors.RED
                    + f" {client_info['stock'][company]['earning_rate']} %"
                    + Colors.RESET
                )
            if client_info["stock"][company]["earning_rate"] == 0:
                print(
                    "\n"
                    f"{company}".ljust(10)
                    + f"매수 : {client_info['stock'][company]['buy_price']:,} ({client_info['stock'][company]['amount']:,}주),  현재가 : {stock_info[company]['now_price']:,} ".ljust(
                        10
                    )
                    + f" {client_info['stock'][company]['earning_rate']} %"
                )
            if client_info["stock"][company]["earning_rate"] < 0:
                print(
                    "\n"
                    f"{company}".ljust(10)
                    + f"매수 : {client_info['stock'][company]['buy_price']:,} ({client_info['stock'][company]['amount']:,}주),  현재가 : {stock_info[company]['now_price']:,} ".ljust(
                        10
                    )
                    + Colors.BLUE
                    + f" {client_info['stock'][company]['earning_rate']} %"
                    + Colors.RESET
                )
