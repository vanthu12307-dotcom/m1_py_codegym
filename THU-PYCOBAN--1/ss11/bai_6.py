def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def hien_thi_so_nguyen_to(n):
    for i in range(1, n + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
n = int(input("Nhập n: "))
hien_thi_so_nguyen_to(n)