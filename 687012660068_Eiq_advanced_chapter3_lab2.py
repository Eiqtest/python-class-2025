import random

set_secret = random.randint(1, 100)
for attempts in range(1, 8):
    answer = int(input(f'Attempt {attempts}/7: Guess the number (1-100): '))
    if answer == set_secret:
        print("Congratulations! You guessed the number.")
        break
    elif answer < set_secret:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
else:
    print(f"Sorry, you’ve used all attempts. The correct number was {set_secret}.")

