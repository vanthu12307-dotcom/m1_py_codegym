numbers = []
for i in range(10):
    num = int(input("Nhập vào số nguyên: "))
    numbers.append(num)
n = int(input("Nhập số n: "))
if n in numbers:
    numbers.remove(n)
    count = 0 
    for n in numbers:
        if n > 5:
           count +=1 
print("List sau khi xử lý:", numbers)
print("Số phần tử > 5 là:", count)