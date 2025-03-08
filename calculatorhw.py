num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

def addition(num1,num2):
    return num1+num2

def multiplication(num1,num2):
    return num1*num2

print("Select operation")
print("1.Addition","2.Multipliction")

operation = int(input("Enter choice of operation 1/2:"))

if operation == 1:
    print(num1,"+",num2,"=",addition(num1,num2))

elif operation == 2:
    print(num1,"*",num2,"=",multiplication(num1,num2))

else:
    print("invalid input")         

 