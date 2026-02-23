jahr = int(input("Nhập số năm: "))
if (jahr%4==0 and jahr%100 !=0) or jahr%400==0 :
    print("Năm", jahr, "là năm nhuận")
else: 
    print("Năm", "không phải là năm nhuận")