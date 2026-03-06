import number_utils as mu
n = int(input("Nhập một số: "))
print("Số đó có phải số chẵn không:", mu.is_even(n))
print("Số đó có phải số lẻ không:", mu.is_odd(n))
print("Số đó có phải số nguyên tố không:", mu.is_prime(n))