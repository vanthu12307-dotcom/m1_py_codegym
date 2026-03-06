def tong_so_chan(n):
    tong = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            tong += i
    print(f"Tổng các số chẵn từ 0 đến {n} là: {tong}")
n = int(input("Nhập số nguyên: "))
tong_so_chan(n)