even_number = 0
odd_number = 0 
while True:
    number = float(input("Enter an integer (0 to quit): "))
    round(number)
    if  number == 0:
        break
    if number %2 == 0:  
        even_number += 1
    else: 
        odd_number += 1
print("Total even numbers:", even_number)
print("Total odd numbers:", odd_number)
        