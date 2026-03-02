import random
a = random.randint(0,10)
solandoan = 0 
sogioihan= 3 
while solandoan < sogioihan:
    doan = int(input("nhập vào số dự đoán: "))
    solandoan += 1 
    if a == doan:
        print("chúc mừng người thắng cuộc và kết thúc trò chơi")
        break
    elif a < doan:
        print("số đã dự đoán đang lớn hơn số bí mật")
    elif a > doan:
        print("số đã dự đoán đang nhỏ hơn số bí mật")
else:
    print("kết thúc trò chơi, bạn đã thua cuộc")
