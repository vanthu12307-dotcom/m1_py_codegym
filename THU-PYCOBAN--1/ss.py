import tkinter as tk
from tkinter import messagebox
import csv
import os

# Hàm xử lý khi nhấn nút Submit
def submit_form():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    day = day_var.get()
    month = month_var.get()
    year = year_var.get()

    # Kiểm tra dữ liệu
    if not name or not phone or not email:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    dob = f"{day}/{month}/{year}"

    file_exists = os.path.isfile("khuyenmai.csv")

    # Ghi file CSV
    with open("khuyenmai.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Ghi header nếu file chưa tồn tại
        if not file_exists:
            writer.writerow(["Họ tên", "SĐT", "Email", "Ngày sinh"])
        
        writer.writerow([name, phone, email, dob])

    messagebox.showinfo("Thành công", "Đăng ký thành công!")

    # Xóa dữ liệu sau khi submit
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
root = tk.Tk()
root.title("Form Đăng ký Khuyến mãi")
root.geometry("400x400")
tk.Label(root, text="ĐĂNG KÝ NHẬN KHUYẾN MÃI", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Họ và tên:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)
tk.Label(root, text="Số điện thoại:").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack(pady=5)
tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)
tk.Label(root, text="Ngày sinh:").pack(pady=5)
frame_dob = tk.Frame(root)
frame_dob.pack()
day_var = tk.StringVar(value="Ngày")
day_menu = tk.OptionMenu(frame_dob, day_var, *[str(i) for i in range(1, 32)])
day_menu.pack(side="left", padx=5)
month_var = tk.StringVar(value="Tháng")
month_menu = tk.OptionMenu(frame_dob, month_var, *[str(i) for i in range(1, 13)])
month_menu.pack(side="left", padx=5)
year_var = tk.StringVar(value="Năm")
year_menu = tk.OptionMenu(frame_dob, year_var, *[str(i) for i in range(1980, 2026)])
year_menu.pack(side="left", padx=5)
tk.Button(root, text="Đăng ký nhận khuyến mãi", command=submit_form).pack(pady=20)
root.mainloop()