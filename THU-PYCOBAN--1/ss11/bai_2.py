import math
def tinhchuvi(r):
    return 2 * math.pi * r
def tinhdientich(r):
    return math.pi * r * r
r = float(input("Nhập bán kính: "))
chuvi = tinhchuvi(r)
dientich = tinhdientich(r)
print("Chu vi hình tròn:", chuvi)
print("Diện tích hình tròn:", dientich)