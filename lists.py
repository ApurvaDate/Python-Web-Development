#Build simple word replacement program
sentence= input('enter your sentence: ')
print("your sentense is : "+sentence)
word1=input("enter word to replace: ")
word2=input("enter the word to replace it with: ")
print(sentence.replace(word1,word2))

#Lists in python

countries= ["UK","India","Ghana","Nigeria","Australia"]
print(countries)
print(countries[0])
print(countries[1:])
print(type(countries))
#to change value from the list
countries[0]="United states"
print(countries)
print(len(countries))

countries=["United Kingdom",2,True,"Australia"]
print(type(countries))

countries=list(("India",34,False))   #list constructor
print(countries)
#list methods

list1=[1,2,3,4,5]
list2=["Banana","apple","mango","orange"]

#to join two lists
list1.extend(list2)
list1

# to add something in a list
list2.append("cherry")
len(list2)

#to add a value in between a list
list2.insert(2,"cherry")
list2.remove("Banana")
list2.clear()
print(list2.index("mango"))
print(list2.count("mango"))

list1=[2,4,5,3,1]
list1.sort()
print(list1)

#to reverse the list
list2.reverse()
list2
#to duplicate a list
list3=list2.copy()
list3
#to remove 
list2.pop(1)
del list2[0]
list2
