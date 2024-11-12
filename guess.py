import random 
import math

def get_user_input():
    while True:
        try:
            return int(input("Enter your guess :"))
        except ValueError:
            print("Invalid input. Please enter an integer.")
def play_game():
    print("Welcome to the Guess the Number Game!")
    print("choose athe range of the number to guess(e.g 1-10)")
    
    while True:
        try:
            min_range= int(input( 'Enter the minimum range: '))
            max_range= int(input( 'Enter the maximum range: '))
            if min_range <0 or max_range < 0:
                print(" enter a positive number please ")
            elif min_range >= max_range:
                print ("min range should be less than max range ")
            else :
                break
        except ValueError:
            print("Invalid input. Please enter integers.")
    
    secret_number = random.randint(min_range, max_range)
    chances = math.ceil(math.log2(max_range - min_range + 1))
    print(f"you got {chances} chances to guess the number between {min_range} and {max_range}")
    
    guess_counter= 0
    while guess_counter < chances:
        guess_counter += 1
        my_guess = get_user_input()
        if my_guess<min_range or my_guess>max_range:
            guess_counter -= 1
            continue
        
        if my_guess == secret_number:
            print(f'the secret number is {secret_number}, you guessed it correctly')
            break
        if my_guess != secret_number:
            if my_guess < secret_number:
                print('Too low, guess higher')
            elif my_guess > secret_number:
                print('Too high, guess lower')
    else:
        print(f'Sorry, you ran out of chances. The secret number was {secret_number}')
    
    play_again = input("Do you want to play again? (yes/no):")
    if play_again.lower() == 'yes':
        play_game() 
play_game() 