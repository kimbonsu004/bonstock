from client import *


def stream():

    for key in clientData['stock'].keys():
        current = clientData['stock'][key]['currentprice']
        print(f'{key} 현재 주가 : {current}')
