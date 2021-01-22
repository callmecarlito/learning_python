#Udemy - 2021 Complete Python Bootcamp From Zero to Hero in Python
#Lecture 55
#Lambda, Map, and Filter functions

my_nums = [i for i in range(20)]
print("Original list:")
print(my_nums)

#Map Function - applies a given function to each item of a given iterable and returns a map object
print("Using mapping:")

def square(num):
    return num**2

print([value for value in map(square, my_nums)])

#Filter Function - applies a given function to each item of a given iterable and returns boolean values
print("Using filtering:")

def check_even(num):
    return num%2 == 0

print([value for value in filter(check_even, my_nums)])

#Lambda Function - small anonymous function used when we require a nameless function for a short period of time
#when using lambda expressions in place of a defined function,
#it must still be easily readable
print("Using Lambda Expressions:")

print([num for num in map(lambda x:x**2, my_nums)])
print([value for value in filter(lambda x:x%2 == 0, my_nums)])

my_names = ["Roberto", "Jessica", "Deangelo"]
print([name for name in map(lambda x:x[::-1], my_names)])