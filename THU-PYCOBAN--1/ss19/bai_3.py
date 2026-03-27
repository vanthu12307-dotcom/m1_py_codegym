class Sinhvien:
    def __init__(self,ma,ten,tuoi):
        self.ma = ma
        self.ten = ten
        self.tuoi = tuoi
    def __str__(self):
        return f"Mã: {self.ma}, Tên: {self.ten}, Tuổi: {self.tuoi}"
while True:
    try:
        tuoi = int(input("Nhập tuổi sinh viên: "))
        if tuoi == 0:
            print("Lỗi: Hãy nhập tuổi lớn hơn 0")
            continue
        break
    except ValueError:
        print("Lỗi : Nhập sai kiểu giá trị")

        