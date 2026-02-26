n = int(input("Nhập số lượng n: "))
a = 0
b = 1
dem = 0
while dem < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    dem += 1