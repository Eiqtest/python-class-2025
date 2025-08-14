# # function
# # part1 import library
# import numpy as np

# #  part 2 -define global variables
# x = 10

# # part 3 - define functions
# def greeting()
#     print("Hello,welcome!")

# part 4 = main program logic

#python function
def greeting(): 
    print("hello,welcome to program!")

def add_number(a=1 , b=1):
    print("the sum is:", a+b)

def subtract_number(a=0, b=0):
    return a-b # use to store number

def add_numbers(a=1, b=2, c=3):
    print("the sum of 3 is:", a + b - c)

import modules as mm
  


# greeting()
# add_number(5 , 10)
# add_number(10 , 8)
# add_number()
# add_numbers()
# total=subtract_number(10, 5)
# print("the result of subtraction is:",total)
print("Factorial of 5 is:", mm.factorial(5))
print("Adding number", mm.add_numbers())
print("Adding number", mm.add_numbers(5,4,3))