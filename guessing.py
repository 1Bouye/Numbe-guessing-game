import random
import math

def get_user_guess():
    while True:
        try:
            return int(input('Please Enter your Guess : '))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def play_game():
    print("Hi welcome to the game, This is a number guessing game.")
    print("Please choose the range of the number to guess (e.g., 1-10, 1-100, etc.)")

    while True:
        try:
            min_range = int(input('Enter the minimum value of the range: '))
            max_range = int(input('Enter the maximum value of the range: '))
            if min_range < 0 or max_range < 0:
                print("Please enter non-negative numbers.")
            elif min_range >= max_range:
                print("The minimum value should be less than the maximum value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter whole numbers.")

    number_to_guess = random.randint(min_range, max_range)
    chances = math.ceil(math.log2(max_range - min_range + 1))

    print(f"You got {chances} chances to guess the number between {min_range} and {max_range}. Let's start the game")

    guess_counter = 0

    while guess_counter < chances:
        guess_counter += 1
        my_guess = get_user_guess()

        if my_guess < min_range or my_guess > max_range:
            print(f"Please enter a number between {min_range} and {max_range}.")
            guess_counter -= 1
            continue

        if my_guess == number_to_guess:
            print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
            break

        elif my_guess > number_to_guess:
            print('Your guess is higher ')

        elif my_guess < number_to_guess:
            print('Your guess is lesser')

    else:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')

    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()

play_game()