client = {"name":"","money":0,}

if client['name'] is not str:
    client["name"] = input("고객님의 성함을 입력해주세요 >> ")
    print("{} 님 반갑습니다.".format(client["name"]))

else:
    pass

if client['money'] == 0:
    client["money"] = int(input("투자하실 금액을 입력해주세요 >>  "))
    print("{} 원 입금되었습니다.".format(client["money"]))

else:
    pass


