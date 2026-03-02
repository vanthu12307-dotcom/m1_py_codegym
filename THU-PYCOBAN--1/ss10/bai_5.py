mkhau = "381"
for i in range(10):
    for j in range(10):
        for k in range(10):
            T = str(i) + str(j) + str(k)
            print("trying", T)
            if T == mkhau:
                print("passwort found: ", T)
                break
        else:
            continue
        break
    else:
        continue
    break