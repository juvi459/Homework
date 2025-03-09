print("for multiplication and division only the first number and second number are required so enter 0 for the rest of the 3 numbers")


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
num4 = int(input("Enter fourth number"))
num5 = int(input("Enter fifth number"))


def addition(num1,num2,num3,num4,num5):
    return num1+num2+num3+num4+num5

def subtraction(num1,num2,num3,num4,num5):
    return num1-num2-num3-num4-num5

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

avg=[num1,num2,num3,num4,num5]

def average(avg):
    return sum(avg) / len(avg)

print("Select operation")
print("1.Addition\n"\
      "2.Subtraction\n"\
        "3.Multiplication\n"\
            "4.Division\n"\
                "5.Average\n")

operation = int(input("Enter choice of operation 1/2/3/4/5:"))

if operation ==1:
    print(num1,"+",num2,"+",num3,"+",num4,"+",num5,"=",addition(num1,num2,num3,num4,num5))

elif operation ==2:
    print(num1,"-",num2,"-",num3,"-",num4,"-",num5,"=",subtraction(num1,num2,num3,num4,num5))

elif operation ==3:
    print(num1,"*",num2,"=",multiplication(num1,num2))

elif operation ==4:
    print(num1,"/",num2,"=",division(num1,num2))

elif operation ==5:
    print("average of",num1,num2,num3,num4,num5,"=",average(avg))

else:
    print("invalid input")         
    
    








