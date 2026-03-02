a = int(input("Nhập một số nguyên dương: "))
if a <= 1:
    print(a, "không phải là số nguyên tố.")
else:
    la_so_nguyen_to = True 
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(a, "là số nguyên tố.")
    else:
        print(a, "không phải là số nguyên tố.")