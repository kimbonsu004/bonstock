clientData = {

    "name":"김본수",

    "money":10000000,
    
    "stock":{
        "apple":
            {
                "buyprice":0,
                "currentprice":0,
                "capacity":5,
            },
            "hansei":
            {
                "buyprice":0,
                "currentprice":0,
                "capacity":0,
            },
        "samsung":
            {
                "buyprice":0,
                "currentprice":0,
                "capacity":0,
            },
        
        "tessla":
            {
                "buyprice":0,
                "currentprice":0,
                "capacity":0,
            },
        
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