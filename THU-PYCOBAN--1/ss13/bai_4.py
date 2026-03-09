numbers = []
for i in range(10):
    num = int(input("Nhập vào số nguyên: "))
    numbers.append(num)
    count = 0 
    for n in numbers:
        if n > 5:
           count +=1 
print("danh sách phần tử là: ", numbers)
print("tất cả các số lớn hơn 5 là: ", count )