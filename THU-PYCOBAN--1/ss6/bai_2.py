a =float(input("nhap so a: "))
b =float(input("nhap so b: "))
c =float(input("nhap so c: "))
if a==b==0 or b**2-4*a*c <0:
    print(" phương trình vô nghiệm")
elif a==0:
    print("phương trình có một nghiệm là", (-c/b))
else:
    print(" phương trình có hai nghiệm")