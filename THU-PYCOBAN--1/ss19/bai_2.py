try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Lỗi không tìm thấy file")
finally:
    print("Kết thúc chương trình")
    