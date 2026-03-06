import password_utils as pw
a = input("Nhập mật khẩu từ bàn phím: ")
if pw.is_strong_password(a) == True:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")