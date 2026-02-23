a = float(input("Nhập số tiền gửi:"))
b = int(input("Nhập số năm gửi:"))
c = float(input("Nhập lãi suất năm (%):"))
T = a*(1+c/100)**b
print("Kết quả:", T )