from company import *

def PL():

    apple_begining = Apple.price()

    while True:

        apple_curret = Apple.current_price(apple_begining)    

        if apple_begining>apple_curret: # 손해일 경우
            lost=round(((apple_curret/apple_begining*100) - 100),3)
            print("\rApple 매수액 : {0:,}   현재가 : {1:,}  수익률 : {2}% ".format(apple_begining,apple_curret,lost),end="")

        elif apple_begining<apple_curret: # 이익일 경우
            profit=round(((apple_curret/apple_begining*100) - 100),3)
            print("\rApple 매수액 : {0:,}   현재가 : {1:,}  수익률 : + {2}% ".format(apple_begining,apple_curret,profit),end="")