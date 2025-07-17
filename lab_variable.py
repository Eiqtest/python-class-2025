# Lab: Python Variables

# 1. Assign values to variables of different types
integer_var = 10
float_var = 3.14
string_var = "Hello, Python!"
boolean_var = True

# 2. Print the values and types of each variable
print("integer_var:", integer_var, type(integer_var))
print("float_var:", float_var, type(float_var))
print("string_var:", string_var, type(string_var))
print("boolean_var:", boolean_var, type(boolean_var))

# 3. Change the value of a variable and print again
integer_var = 20
print("Updated integer_var:", integer_var)

# 4. Demonstrate variable naming rules
snake_case_var = 5
CamelCaseVar = 6
# 5snake = 7  # Invalid: cannot start with a number
# my-var = 8  # Invalid: cannot use hyphens

# 5. Input and Output
user_name = input("Enter your name: ")
print("Hello, ", user_name)

# 6. Type conversion
num_str = "123"
num_int = int(num_str)
print("Converted string to int:", num_int, type(num_int))

# 7. Constants (by convention)
PI = 3.14159
MAX_SPEED = 120
print("PI:", PI)
print("MAX_SPEED:", MAX_SPEED)
