a = int(input("Nhập số nguyên: "))
b = int(input("Nhập số nguyên: "))
c = int(input("Nhập số nguyên: "))
max = a if a>b and a>c else b if b>c else c 
print(max)