weight = float(input("Enter Your Weight: "))
height = float(input("Enter Your Height: "))

def BMI_Calculator():
    BMI = weight/height**2
    print("Your BMI is : ",BMI)

BMI_Calculator()

#With multiparameter

def BMI_Calculator(weight,height):
    BMI = weight/height**2
    print("Your BMI is : ",BMI)

BMI_Calculator(64,1.7)