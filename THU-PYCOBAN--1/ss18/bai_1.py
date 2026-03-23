import csv
def nhap_du_lieu():
    danh_sach = []
    for i in range(5):
        print(f"\nNhập thông tin người thứ {i+1}:")
        ten = input("Tên: ")
        tuoi = input("Tuổi: ")
        dia_chi = input("Địa chỉ: ")
        danh_sach.append([ten, tuoi, dia_chi])
    return danh_sach

def ghi_file_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Tên", "Tuổi", "Địa chỉ"])
        writer.writerows(data)
def doc_file_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
ds = nhap_du_lieu()
ghi_file_csv("data.csv", ds)
print("\nDữ liệu đã ghi vào file\n")
print("Đọc dữ liệu từ file:")
doc_file_csv("data.csv")