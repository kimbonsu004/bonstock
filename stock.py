stock_info = {
    "apple": {"start_price": 0, "now_price": 0, "change_rate": 0},
    "hansei": {"start_price": 0, "now_price": 0, "change_rate": 0},
    "samsung": {"start_price": 0, "now_price": 0, "change_rate": 0},
    "tessla": {"start_price": 0, "now_price": 0, "change_rate": 0},
    "theori": {"start_price": 0, "now_price": 0, "change_rate": 0},
}


class Colors:
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"


def show_stock_info():
    for company in stock_info.keys():
        stock_info[company]["change_rate"] = round(
            stock_info[company]["now_price"] / stock_info[company]["start_price"] * 100 - 100, 2
        )
        if stock_info[company]["change_rate"] > 0:
            print(
                "\n"
                f"{company}".ljust(10)
                + f"시초가 : {stock_info[company]['start_price']:,},  현재가 : {stock_info[company]['now_price']:,} ".ljust(
                    5
                )
                + Colors.RED
                + f" {stock_info[company]['change_rate']} %"
                + Colors.RESET
            )
        if stock_info[company]["change_rate"] == 0:
            print(
                "\n"
                f"{company}".ljust(10)
                + f"시초가 : {stock_info[company]['start_price']:,},  현재가 : {stock_info[company]['now_price']:,} ".ljust(
                    5
                )
                + f" {stock_info[company]['change_rate']} %"
            )
        if stock_info[company]["change_rate"] < 0:
            print(
                "\n"
                f"{company}".ljust(10)
                + f"시초가 : {stock_info[company]['start_price']:,},  현재가 : {stock_info[company]['now_price']:,} ".ljust(
                    5
                )
                + Colors.BLUE
                + f" {stock_info[company]['change_rate']} %"
                + Colors.RESET
            )


def get_stock_list():
    stock_list = {company for company in stock_info.keys()}
    return stock_list
