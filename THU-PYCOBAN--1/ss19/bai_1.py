try:
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    c = a/b 
except ZeroDivisionError:
    print("Lỗi nhập số 0")
except ValueError:
    print("nhập sai giá trị")
finally:
    print("Kết thúc chương trình")
