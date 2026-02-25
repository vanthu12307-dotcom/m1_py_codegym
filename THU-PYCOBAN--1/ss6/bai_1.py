lohn = float(input("Nhập lương nhân viên: "))
if lohn == 15000:
    tax = lohn *30/100
elif 7000 <= lohn < 15000 :
    tax = lohn *20/100
elif lohn < 7000:
    tax = lohn *10/100
b = lohn - tax
print("số tiền lương:", b )