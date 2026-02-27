import turtle
tt= turtle.Turtle
for i in range(7):
    for j in range(21):
        if i==0 or i==6 or j==20 or j==0:
           print("*", end='')
        else:
            print(" ", end='')
    print("")