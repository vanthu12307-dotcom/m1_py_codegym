friends = []
def show_menu():
    print("\nQUẢN LÝ BẠN BÈ FACEBOOK")
    print("1. Hiển thị danh sách bạn bè")
    print("2. Thêm bạn bè")
    print("3. Chỉnh sửa tên bạn bè")
    print("4. Xóa bạn bè")
    print("0. Thoát")
#dsach 
def show_friends():
    if len(friends) == 0:
        print("Danh sách bạn bè trống.")
    else:
        print("\nDanh sách bạn bè:")
        for i, friend in enumerate(friends):
            print(f"{i+1}. {friend}")
#thêm bbe
def add_friend():
    name = input("Nhập tên bạn bè mới: ")
    friends.append(name)
    print("Đã thêm bạn bè thành công.")
#sửa tên
def edit_friend():
    show_friends()
    if len(friends) == 0:
        return
    try:
        index = int(input("Nhập số thứ tự bạn muốn sửa: ")) - 1
        if 0 <= index < len(friends):
            new_name = input("Nhập tên mới: ")
            friends[index] = new_name
            print("Đã cập nhật tên bạn bè.")
        else:
            print("Không hợp lệ.")
    except:
        print("Vui lòng nhập số.")
#xóa bbe
def delete_friend():
    show_friends()
    if len(friends) == 0:
        return
    try:
        index = int(input("Nhập số thứ tự bạn muốn xóa: ")) - 1
        if 0 <= index < len(friends):
            removed = friends.pop(index)
            print("Đã xóa bạn:", removed)
        else:
            print("Không hợp lệ.")
    except:
        print("Vui lòng nhập số.")
#Chương trình chính
while True:
    show_menu()
    choice = input("Chọn chức năng: ")
    if choice == "1":
        show_friends()
    elif choice == "2":
        add_friend()
    elif choice == "3":
        edit_friend()
    elif choice == "4":
        delete_friend()
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")