import random

again = "y"

while again == "y":
    print("Rolling the dice...")
    print("The value is: ", random.randint(1, 6))

    again = input("Roll the dice again? (y/n): ")
