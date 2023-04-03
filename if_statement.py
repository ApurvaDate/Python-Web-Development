#if statements in python
#if statement gives a condition
value=input("Input a value : ")

#to check whether it is a string
if type(value)==str:
    print(value+ " is a string")
elif type(value)==int:
    print(value+ " is an integer")
elif type(value)==list:
    print(value+"is a list")
else:
    print("we dont know the data type of "+value)
#this prints only string as it takes input as a string


#now to check only for string
#to check whether it is a string
value=int(input("input a value: "))

if type(value)==str:
    print("it is a string")
else:
    print('it is not a string')

#to check whether it is divided by 5 or not
#% operator gives us reminder

value=int(input())
if value%5==0:
    print(str(value)+" is divisible by 5")
else:
    print(str(value)+" is not divisible by 5")

#Building a python program to check if a number is an even number or not

number=int(input("enter a number"))
if number%2==0:
    print(str(number)+" is an even number")
else:
    print(str(number), " is an odd number")

