#Dictionaries in python

my_dict={ "name":"tim","nationality":"indian","qualification":"college"}
print(my_dict)
print(my_dict["name"])

#if we add name again in the dictionary it will print the latest name and not previous name
my_dict={ "name":"tim","nationality":"indian","qualification":"college","age":25,"astall":True,"friends":["Peter","Paul","Precious"]}
print(my_dict["name"])
print(len(my_dict))
print(my_dict["age"])
print(my_dict["astall"])
print(my_dict["friends"])
print(type(my_dict))

#While loops in python

i=1
while i < 6 or i==6 :
    print(i)
    i+=1

#for loop in python

for letter in "Hello":
    print(letter)

my_list=["ji","ju","jo"]
for x in my_list:
    print(x)
for x in my_dict:
    print(x)  #it prints the keys

for x in my_list:
    if x=="ju":
        break
    print(x)

for x in range(4):
    print(x)
for x in range(3,7):
    print(x)

for x in range(7):
    print(x)
else:
    print("finished looping")




