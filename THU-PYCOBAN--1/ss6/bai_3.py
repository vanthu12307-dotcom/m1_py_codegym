ds = float(input("Nhập tổng doanh số bán được: "))
if ds <= 100:
    hh = ds * 5/100
elif ds <= 300:
    hh = ds *10/100
elif ds >300:
    hh = ds *20/100
T = ds - hh
print("Tổng số tiền hoa hồng là", T)