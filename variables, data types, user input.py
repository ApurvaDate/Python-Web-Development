
"""""
In this we learnt about python variables, data types, numbers and user input
"""""


from math import *  #this will import everything from math
print("Hello World!")
print("hello World \n Welcome!")

#Python variables

#which are used as a reference

print("Tim is a boy!")
print("Tim is 18")
print("Tim is from Turkey")

name="Tim"

print(name+"is a boy")
print(name+" is 18")
print(name+" is from Turkey")

# there are different data types in python

age=18
print(name + " is "+ str(age))

#strings in python

#it is just a plain text,we can also print string as a variable
print("Hi.\nHow are you?")
print(name)

#functions in python is just a block of code which does a particular task
print(name[0])  #number count starts from 0
print(name[2])
name.upper()
name.lower()
print(name.islower())
print(name.isupper())
print(name.lower().islower())

#to find amount of characters present
len(name)  #len of string
print(name.replace("m","t"))

#numbers in python
print(17)
#we can also specify number as a variable
number=79
print(number)
#add numbers
print(78+22.323)
print(78-22.323)
print(78/2)
print(78//2)

print(20/6)
print(20%6)#to find reminder of division
number=22
number2=55
print(number+number2)
print(number+str(number2))
print(-5)
print(abs(-5))
print(max(4,-2))
print(min(2,8,0,1))
print(round(3.2))
print(round(3.5))
print(bin(3)) #which gives binary string 
print(sqrt(100))

#Getting users input

#input a text, save that into a variable 
name=input('Input your name: ' )
age=input('Input your age: ')
print('Your name is '+name+' and your age is '+age)

#we can convert this age into integer
age=int(input("Input your age: "))
print('Your name is '+name+' and your age is ',age)
