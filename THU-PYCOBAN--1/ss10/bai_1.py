n = int(input("Nhập vào số nguyên: "))
if n < 0:
    print(n, " Không phải là giai thừa")
else: 
    a = 1 
    for i in range(1,n + 1):
        a *= i
        print(f"{n}! = {a}")
print("nhập số hợp lệ")