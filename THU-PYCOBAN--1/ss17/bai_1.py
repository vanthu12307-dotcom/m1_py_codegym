import tkinter as tk
def dang_nhap():
    name = entry.get()
    label_kq.configure(text=f"Bạn đã nhập tên đăng nhập là: {name}")
window = tk.Tk()
window.title("First_Program")
window.geometry("400x200")
label_kq = tk.Label(window, text="")
label_kq.pack()

label = tk.Label(window, text="Tên của bạn")
label.place(x=80,y=50)
entry = tk.Entry(window, width=30)
entry.place(x=155,y=50)
btn = tk.Button(window, text="Đăng nhập", command=dang_nhap)
btn.place(x=155,y=70)
window.mainloop()