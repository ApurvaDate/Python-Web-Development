# ################  classes and objects ##############

# classes are like feature or functions in python
# more precisely we can say that classes are constructor of objects
class Myclass:
    x = 5  # x is an object here/attribute
p1= Myclass()  # initialize
print(p1.x) #this will print 5 

#init function
#it helps us to initialize different values in our class

class person:
    def __init__(self,name,age):
            self.name=name
            self.age=age

p1=person('apurva',25)
print(p1.name)
# print(p1.age)

name=input("Enter your name")
age=input("Enter your age")
p2=person(name,age)
print(p2.name)
print(p2.age)

#to delete age from the class an object

del p1.age  #this will remove age
print(p1.name)


#if we dont know the attributes of the class we can use pass
class person:
    pass
#if we dont use pass we get an error


######### inheritance ############

# it means taking info from the existing class and using or getting it for a new class

class student:
     name="tim"
     age=24
     gender="male"

#to use below code in a new py file to access student class attributes in a new class
# from Classes_objects import student

# class person(student):
#     pass

# p1=person()
# print(p1.name)
# print(p1.age)
# print(p1.gender)

#this is what python inheritance is.
