clientData = {

    "name":"김본수",

    "money":10000000,
    
    "stock":{
        "samsung":
            {
                "buyprice":3000,
                "currentprice":0,
                "capacity":5,
            },
        "apple":
            {
                "buyprice":4000,
                "currentprice":0,
                "capacity":5,
            },
        "tessla":
            {
                "buyprice":0,
                "currentprice":0,
                "capacity":0,
            },
        "hansei":
            {
                "buyprice":2000,
                "currentprice":0,
                "capacity":5,
            }
        }    
}

def client():

    if clientData['name'] == "":
        clientData["name"] = input("고객님의 성함을 입력해주세요 >>> ")

    else:
        pass

    if clientData['money'] == 0:
        clientData["money"] = int(input("고객님이 투자하실 금액을 입력해주세요 >>> "))

    else:
        pass
 
    my_name = clientData["name"]
    my_money = clientData["money"]
    my_stock = clientData["stock"]

    return my_name,my_money,my_stock    