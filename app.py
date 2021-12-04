from client import check_client_nulldata, show_client_info, show_client_earninginfo
from company import set_company_start_price
from stock import show_stock_info
from trade import set_trade
import os


def start_app_service():
    set_company_start_price()
    check_client_nulldata()


def select_app_service(num):
    if num == 1:
        set_trade()  # 주식 거래
    if num == 2:
        show_stock_info()  # 주가 현황
    if num == 3:
        show_client_info()  # 자산 현황
    if num == 4:
        show_client_earninginfo()  # 실현 손익

    if num == 99:
        os.system("cls")


if __name__ == "__main__":
    start_app_service()

    print(
        """
    ______                _____  _                 _    
    | ___ \              /  ___|| |               | |   
    | |_/ /  ___   _ __  \ `--. | |_   ___    ___ | | __
    | ___ \ / _ \ | '_ \  `--. \| __| / _ \  / __|| |/ /
    | |_/ /| (_) || | | |/\__/ /| |_ | (_) || (__ |   < 
    \____/  \___/ |_| |_|\____/  \__| \___/  \___||_|\_\
                                                        
                                                                                                    
    Python mock stock trading program by "kimbonsu004"
    Developer Github : https://github.com/kimbonsu004
    Thank you for using my program  。˚˚✧₊ ⁎⁺˳✧༚ ♡ミ
    """
    )
    while True:
        try:
            print(
                """
        [1] : 주식 거래
        [2] : 주가 현황
        [3] : 자산 현황
        [4] : 실현 손익
        [99] : 정리
            """
            )
            num = int(input("원하시는 서비스를 선택하여 주세요 >> "))
            select_app_service(num)
        except ValueError:
            print("잘못된 입력입니다.")
            continue
        except KeyboardInterrupt:
            print()
            continue
