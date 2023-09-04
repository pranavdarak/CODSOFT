print("Welcome to the calculator")

num1 = float(input("Enter the first number: "))
num2 =  float(input("Enter the second number: "))
op = input("Enter the operation you want to perform : ")

if op == "+":
    print(num1+num2)
    
elif op == "-":
    print(num1-num2)

elif op == "*":
    print(num1*num2)

elif op == "/":
    print(num1/num2)

elif op == "**":
    print(num1**num2)

else:
    print("Invalid Input")
