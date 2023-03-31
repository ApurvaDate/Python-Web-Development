#Tuples in python

#tuples are used to store multiple items in a single variable
#tuples are immutable that means we cannot change any value from it.
three_numbers=(1,2,3,1)
three_numbers
three_numbers[0]
three_numbers[0]=23 #which gives an error, so we cannot change it.
#tuples allow repetition of same value
print(len(three_numbers))
type(three_numbers)
#tuples allow multiple data types



#*********** functions in python *************
#functions are nothing but a block of code which performs particular task.
def greetings_function():
    print("Welcome  User")
greetings_function()

def greetings_function(name,age):
    print("Welcome "+name+". You are "+str(age)+" years old")
greetings_function("apurva",26)

#in case we dont know how many parameters are there in the function 
def greetings_function(*names):
    print("Welcome "+names[1]) 
greetings_function("John","sid","Tim")

def greetings_function(name,age):
    print("Welcome "+name+". You are "+str(age)+" years old")
name=input("Enter your name:")
age=int(input("Enter your age: "))
greetings_function(name, age)


######### the return statement in python
#return statement shows the end of that function
def my_function():
    return 5+4
my_function()

def add_numbers(num1,num2):
    return num1+num2
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
add_numbers(num1,num2)