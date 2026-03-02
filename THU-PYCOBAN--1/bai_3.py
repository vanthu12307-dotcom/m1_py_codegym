n = int(input("Nhập số a : "))
sum= 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print(n, "Là số hoàn hảo")
else:
    print(n, "là số không hoàn hảo")

   