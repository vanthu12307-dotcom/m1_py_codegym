numbers = []
for i in range(10):
    num = int(input("Nhập số nguyên: "))
    numbers.append(num)
max_ = max(numbers)
index = numbers.index(max_)
print("Giá trị lớn nhất trong list numbers là:", max_)
print("Vị trí của phần tử đó trong mảng là:", index)