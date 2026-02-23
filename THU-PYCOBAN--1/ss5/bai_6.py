weight = float(input("Nhập cân nặng: "))
height = float(input("Nhập chiều cao: "))
BMI = weight / (height**2)
if (BMI < 18.5):
    print("Underweight")
elif ( 18.5 <= BMI < 25.0):
    print("Normal")
elif (25.0 <= BMI < 30.0):
    print("Overweight")
elif ( 30.0 <= BMI):
    print("Obese")
