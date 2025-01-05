import random

print("Guess the number between 1 and 100!")
# Generate random number
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess number: "))
        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print("Congratulations! You got it right!")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
