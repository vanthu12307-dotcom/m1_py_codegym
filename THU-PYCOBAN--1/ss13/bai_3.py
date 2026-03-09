numbers = []
for i in range(10):
    num = int(input("Nhập vào số nguyên: "))
    numbers.append(num)
    a = 0 
    for n in numbers:
        if n > 10:
            a += n 
print("danh sách phần tử là: ", numbers)
print("tổng tất cả các số lớn hơn 10 là: ", a )