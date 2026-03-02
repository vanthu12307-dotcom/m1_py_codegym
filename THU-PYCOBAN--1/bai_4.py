a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
sum = 0 
for i in range(1,a ):
    for j in range(1,b ):
        if b % i ==0 and a % i == 0:
            sum += 1
if i != j:
    print(a , "và", b, "là 2 số hoàn hảo")
else:
    print(a , "và", b, "không phải là 2 số hoàn hảo")           