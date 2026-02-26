import random
a= random.randint(1,100)
solandoan = 0 
sogioihan = 7 
while solandoan < sogioihan:
    doan = int(input("Nhập số bạn đoán (1 - 100): "))
    solandoan +=1
    if doan==a:
        print("Chúc mừng! Bạn đã đoán đúng")
        break
    elif doan < a:
        print("Số bạn đoán nhỏ hơn số bí mật")
    else:
        print("Số bạn đoán lớn hơn số bí mật")
else:
    print("Rất tiếc, bạn đã thua. Số đúng là:", a)