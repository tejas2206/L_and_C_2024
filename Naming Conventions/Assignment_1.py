# Please add the meaningful names to the given programs

# Assignment 1: The below program is to Roll the Dice

import random
def roll_dice(sides):
    number = random.randint(1, sides)
    return number

def main():
    sides = 6
    is_rolling = True
    while is_rolling:
        user_input = input("Ready to roll? Enter Q to Quit")
        if user_input.lower() != "q":
            result = roll_dice(sides)
            print("You have rolled a", result)
        else:
            is_rolling = False

#-------------------------------------------------------------------------------------------------------

# Assignment 2: The below program is to guess the correct number between 1 to 100

import random

def is_valid_guess(guess):
    if guess.isdigit() and 1 <= int(guess) <= 100:
        return True
    else:
        return False

def main():
    target_number = random.randint(1, 100)
    guessed_correctly = False
    guess = input("Guess a number between 1 and 100:")
    num_guesses = 0

    while not guessed_correctly:
        if not is_valid_guess(guess):
            guess = input("I won't count this one Please enter a number between 1 and 100")
            continue
        else:
            num_guesses += 1
            guess = int(guess)

        if guess < target_number:
            guess = input("Too low. Guess again")
        elif guess > target_number:
            guess = input("Too high. Guess again")
        else:
            print(f"You guessed it in {num_guesses} guesses!")
            guessed_correctly = True

main()

#-------------------------------------------------------------------------------------------------------

# Assignment 3: The below program is to check whether the number is Armstrong number or not

def calculate_armstrong_sum(number):
    # Initializing Sum and Number of Digits
    armstrong_sum = 0
    num_digits = 0

    # Calculating Number of individual digits
    temp_number = number
    while temp_number > 0:
        num_digits = num_digits + 1
        temp_number = temp_number // 10

    # Finding Armstrong Number
    temp_number = number
    for _ in range(1, temp_number + 1):
        digit = temp_number % 10
        armstrong_sum += digit ** num_digits
        temp_number //= 10

    return armstrong_sum
    
# End of Function

# User Input
input_number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

if (input_number == calculate_armstrong_sum(input_number)):
    print(f"\n{input_number} is an Armstrong Number.\n")
else:
    print(f"\n{input_number} is Not an Armstrong Number.\n")