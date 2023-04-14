#collect three inputs from the user
#num1 ,num2 and the operator

# print("To build a basic calculator")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
op=input("Enter operator:")

if op=="+":
    print("The addition is : ",num1+num2)
elif op=="-":
    print("The subtraction is : ",num1-num2)
elif op=="*":
    print("The multiplication is : ",num1*num2)
elif op=="/":
    print("The division is : ",num1/num2)
else:
    print("invalid operator")