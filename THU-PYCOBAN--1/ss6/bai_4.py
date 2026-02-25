mnt = int(input("Nhập số phút: "))
thue_bao = 25000 
if 1 < mnt <=50:
    p = 600 
elif 50 < mnt <= 150:
    p =  400
elif mnt > 200:
    p =  200
C = thue_bao + p
print("Cước điện thoại là:", C )