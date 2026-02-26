a = float(input("nhập điểm môn học (từ 0 đến 10): "))
while a < 0 or a > 10:
    print("yêu cầu nhập lại")
    a = float(input("nhập điểm môn học (từ 0 đến 10): "))
print("diem mon hoc la:", a )