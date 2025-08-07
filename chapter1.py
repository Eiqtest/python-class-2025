# #  Variables and Data Types
# a = 5   # integer mean number
# b = 5.0 # Float
# c = "Supachai Weawkeaw" # String single word or more
# d = True # Boolean contain only True / False
# e = 6+5 # complex

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a = 55 
# b = 6.5
# print(a)
# print(b)

# z = a+b # Float
# print(z)

# Descriptive name vs meaning full name
# tax = 0.07
# firstname = "Supachai"
# email = "eiqson9904@gmail.com"
# age = 18

# Multi words variable name two more words
# Snake case
# student_first_name = "Supachai"
# StudentName = 'idk'shouldn't or not recommend to do
# student_last_name = 'Weawkeaw'
# student_age = 18
# student_email = 's69xxxxxxson9904@gmail.com'

# Constant variables IT mean fixed value like PIE and Limit speed
# P = 3.14
# Max_speed = 120 

# print("student name:" + student_first_name)
# print(f"Student lastname: {student_last_name}")

# Data Types
# a = 1 #int
# b = 1.1 #float
# c = '1' #string if have single alphabet will count as character instead 

# print(a+a) #2
# print(b+b) #2.2
# print(c+c) #11
# print(a+b) # 2.1
# # print(a+c) # Error Because int and float can't mix with string

# print(type(a)) # Used to check date type if it is int,float or str
# print(type(b))
# print(type(c))

# # Convert Types
# a = float(a) # float
# b = int(b) # int
# c = int(c) # string must only have number and not alphabet
# print(a)
# print(b)
# print(c)
# print(a+c)

# a =  1 FOR EXAMPLE
# a = float(a)
# print(a)

# Scope Variable = Global and local variable
# x = "awesome." # string

# def my_function():
#     x = "fantastic."
#     print("python is " + x)
# my_function()   
# print("Python is " + x)


#Input statement
# Student_name = input("Enter your name:")

# # Output statement
# print("Student name:" + Student_name) # Also can use ("Student name:", Student_name)

# print("Student name:", Student_name) # Using comma to separate string and variable

# INPUT AND OUTPUT
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# print(a+b)

# OR

# a = input("Enter a number: ")
# b = input("Enter another number: ")   
# print(float(a) + float(b))  # Convert input to int before adding

# a = input("Enter a number: ")
# b = input("Enter another number: ") 
# a = int(a)  # Convert input to int
# b = int(b)  # Convert input to int    
# print(a + b)  # Now you can add them as integers

# Operators
# Python divides the operators in the following groups:

#  Assignment operators "="
# a = 5
# b = 10  
# x=z=k= 15
# #  Arithmetic operators "+""
# a = 8
# b = 2 
# a = a + b  # Addition 10
# b = a - b # Subtraction 8 FOR NOW ON B IS 8 CAUSE IT ASSIGN TO "b"
# c = a * b  # Multiplication 80
# d = a / b#Division 1.25
# e = a % b # Modulus 1
# f = a** b# Exponentiation 10^8
# g = a // b# Floor division 2
# print("Addition:", a)
# print("Subtraction:", b)
# print("Multiplication:", c)
# print("Division:", d)
# print("Modulus:", e)
# print("Exponentiation:", f)
# print("Floor division:", g) 

#  Comparison operators
# a = 10
# b = 10.0
# Equal to
# a == b # True if both are equal
# print(a == b)
# # a == b
# print(a == b and type(a) == type(b))  # True if both are equal and of the same type
# print(a == b or type(a) == type(b))  # True if either condition is true
# Not equal to
# print(a != b)  # True if a is not equal to b

# # Greater than
# print(a > b)  # True if a is greater than b

# # Less than
# print(a < b)  # True if a is less than b

# # Greater than or equal to
# print(a >= b)  # True if a is greater than or equal to b

#  Logical operators
# and
# print(a > 5 and b < 15)  # True if both conditions are true

# # or 
# print(a < 5 or b > 15)  # True if either condition is true

# # not
# print(not (a < 5))  # True if the condition is false

# import math

# # 1. Get the value of pi
# print("math.pi:", math.pi)

# # 2. Square root
# print("Square root of 16:", math.sqrt(16)) # 4

# # 3. Power
# print("2 to the power of 3:", math.pow(2, 3)) # 8

# # 4. Trigonometric functions
# print("sin(90 degrees):", math.sin(math.radians(90))) 
# print("cos(0 degrees):", math.cos(math.radians(0)))

# # 5. Logarithm
# print("log(100, base 10):", math.log10(100))

# # 6. Ceiling and floor
# print("Ceiling of 2.3:", math.ceil(2.3))
# print("Floor of 2.7:", math.floor(2.7))

# # 7. Factorial
# print("Factorial of 5:", math.factorial(5))


# #  Identity operators
# #  Membership operators
# #  Bitwise operators

# a = 5 
# print (int(str(a)))