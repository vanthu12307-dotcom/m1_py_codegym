n = int(input("Nhập vào 1 số nguyên: "))
dict =dict({})
for i in range(1,n+1):
    di = i*i 
    dict[i]= di
    di += 1 
print(dict)