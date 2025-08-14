def factorial(n):
    if n <= 1:
        print(1)
        return 1
    else:
        print(f"{n} *")
        return n * factorial(n -1)
    
def add_numbers(a=1, b=2, c=3):
    return a + b - c

   