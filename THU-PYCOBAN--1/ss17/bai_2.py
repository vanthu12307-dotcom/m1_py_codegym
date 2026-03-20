from tkinter import *
def dang_nhap():
    name = entry1.get()
    pas = entry2.get()

    if name =="admin" and pas == "123456":
        username_kq.config(text="đăng nhập thành công")
    else:
        username_kq.config(text="đăng nhập thất bại")
    

login_window = Tk()
login_window.geometry("400x250")
login_window.title("Login-program")
login = Label(login_window, text="login").place(x=30, y=30)
username = Label(login_window, text="username").place(x=30, y=60)
entry1 = Entry(login_window, width=30)
entry1.place(x=30, y= 100)
password = Label(login_window, text="password").place(x=30, y=120)
entry2 = Entry(login_window, width=30)
entry2.place(x=30, y=160)
login = Button(login_window, text="login", width=10, command=dang_nhap).place(x=30, y=200)

username_kq = Label(login_window,text="")
username_kq.pack()
password_kq = Label(login_window,text="")
password_kq.pack()

login_window.mainloop()