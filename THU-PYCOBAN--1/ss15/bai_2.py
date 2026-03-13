thudo_quocgia = []
def show_menu():
    print("\n---------Chương trình quản lý quốc gia và thủ đô----------")
    print("Nhập phím 1 để hiển thị danh sách các quốc gia và thủ đô")
    print("Nhập phím 2 để thêm mới quốc gia và thủ đô")
    print("Nhập phím 3 để xóa quốc gia và thủ đô")
    print("Nhập phím 4 để sửa tên thủ đô")
    print("Nhập phím 5 để tra cứu thủ đô")
    print("Nhập phím 6 để thoát chương trình")
#dsach
def show_qgtd():
    if len(thudo_quocgia) == 0:
        print("Danh sách thủ đô và quốc gia TRỐNG")
    else:
        print("\n Danh sách thủ đô và quốc gia: ")
        for i,thudo_quocgi in enumerate(thudo_quocgia):
            print(f"{i+1}. {thudo_quocgi}")
#thêm thủ đô và quốc gia
def add_thudovaquocgia():
    quoc_gia =input("Nhập tên quốc gia mới: ")
    thu_do = input("Nhập tên thủ đô mới: ")
    thudo_quocgia.append(quoc_gia)
    thudo_quocgia.append(thu_do)
    print("đã thêm quốc gia và thủ đô thành công")
#sửa tên thủ đô và quốc gia
def edit_thudovaquocgia():
    show_qgtd
    if len(thudo_quocgia) == 0:
        return
    try:
        index = int(input("Nhập thủ đô và quốc gia bạn muốn sửa: ")) - 1
        if 0 <= index < len(thudo_quocgia):
            new_name = input("Nhập thủ đô và quốc gia mới: ")
            thudo_quocgia[index] = new_name
            print("Đã cập nhật thủ đô và quốc gia mới.")
        else:
            print("Không hợp lệ.")
    except:
        print("Vui lòng nhập tên thủ đô và quốc gia.")
#xóa quốc gia và thủ đô
def delete_thudovaquocgia():
    show_qgtd
    if len(thudo_quocgia) == 0:
        return
    try:
        index = int(input("Nhập thủ đô và quốc gia bạn muốn xóa: ")) - 1
        if 0 <= index < len(thudo_quocgia):
            removed = thudo_quocgia.pop(index)
            print("Đã xóa thủ đô và quốc gia:", removed)
        else:
            print("Không hợp lệ.")
    except:
        print("Vui lòng nhập lại tên thủ đô và quốc gia.")
#Chương trình chính
while True:
    show_menu()
    choice = input("Chọn chức năng: ")
    if choice == "1":
        show_qgtd()
    elif choice == "2":
        add_thudovaquocgia()
    elif choice == "3":
        edit_thudovaquocgia()
    elif choice == "4":
        delete_thudovaquocgia()
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")