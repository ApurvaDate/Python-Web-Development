# Try and except

x=int(input("Input an integer: "))
print(x)
#if we input a string this gives an error
try:
    x=int(input("Input an integer: "))
    print(x)
except:
    print("something went wrong,please try again")
# or we can also write when its a value error
try:
    x=int(input("Input an integer: "))
    print(x)
except ValueError or NameError:
    print("Value not an integer")
else:
    print('nothing went wrong')
try:
    x=int(input("Input an integer: "))
    print(x)
except ValueError or NameError:
    print("Value not an integer")
finally:
    print('try except finish')  #whether there is error or not this is going to print


#Reading files
print("Hello")

country_file=open('D:/Web_development/countries.txt','r')  #only to read this file not edit
#a means append to the file at the end
#r+ both read and write
print(country_file.readlines())

# for files in country_file.readlines():
#     print(files)

country_file.close() #to close the file


#writing files in python
country_file=open('D:/Web_development/newfile.txt','w')
country_file.write('This is the new file')

newFile=open('D:/Web_development/newfile.txt','a')  #to append 
newFile.write("\n This is a new line")



