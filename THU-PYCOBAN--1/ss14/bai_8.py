t = (1, 2, 2, 3, 2, 4, 5)
def count_number(t, x):
    return t.count(x)

def find_last_position(t, x):
    for i in range(len(t)-1, -1, -1):
        if t[i] == x:
            return i
    return -1
print("Số lần xuất hiện:", count_number(t, 2))
print("Vị trí cuối:", find_last_position(t, 2))