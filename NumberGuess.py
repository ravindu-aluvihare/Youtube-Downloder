import random
import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low.")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high.")
        return attempts - 1
    else:
        print(f"Your guess is right! The answer was {answer}.")
        return 0  # Return 0 to break out of the loop when the guess is correct.

def game():
    print(logo.logo)
    print("Let me think of a number between 1 to 50.")
    answer = random.randint(1, 50)
    # Debugging hint, remove it in production.
    # print(f"Debug: The correct answer is {answer}")
    
    level = input("Choose level - 'Easy' or 'Hard': ").lower()
    attempts = set_difficulty(level)
    
    guessed_number = -1  # Initialize guessed_number to a value not equal to `answer`.

    while guessed_number != answer:
        if attempts == 0:
            print("You are out of guesses - you lose!")
            return
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Guess a number: "))
        
        attempts = check_answer(guessed_number, answer, attempts)

        if guessed_number == answer:
            break
        elif attempts > 0:
            print("Try again.")

# Run the game
game()
