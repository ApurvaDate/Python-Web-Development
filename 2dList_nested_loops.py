#2D lists and nested loops in python
my_list=[1,2,3,4]
print(my_list)

my_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(my_list)
print(type(my_list))
print(my_list[0])
print(my_list[1][1])

for list in my_list:
    for row in list:
        print(row)
#comments in python

'''
my_func():
    print("hi")
'''
print("hello")
print(1)
my_func()

#comments are used in python to make your code more readable

