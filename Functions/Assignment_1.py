# The below program is to guess the correct number between 1 to 100.
import random


def is_valid_number(guessed_number):
    return guessed_number.isdigit() and 1 <= int(guessed_number) <= 100


def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if is_valid_number(user_input):
            return int(user_input)
        print("Invalid input. Please enter a number between 1 and 100.")


def play_game():
    target = random.randint(1, 100)
    guess_count = 0

    print("Guess a number between 1 and 100:")
    while True:
        guess = get_valid_input("Your guess: ")
        guess_count += 1

        if guess < target:
            print("Too low. Try again.")
        elif guess > target:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed it in {guess_count} attempts.")
            break


def main():
    play_game()


if __name__ == "__main__":
    main()
