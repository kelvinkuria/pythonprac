# Importing the 'random' module from Python's standard library.
# This module allows the program to generate random numbers, which are essential for making the game unpredictable.
import random 


# ---------------------- HUMAN GUESSING FUNCTION ----------------------

# Define a function named 'guess' that takes one argument 'x'.
# This function allows the user (human) to guess a random number between 1 and x.
def guess(x):
    # Generate a random number between 1 and x (inclusive).
    # random.randint(a, b) returns an integer between a and b (both inclusive).
    random_number = random.randint(1, x)
    
    # Initialize the variable 'guess' with 0.
    # This is just a placeholder to enter the while loop.
    guess = 0

    # The 'while' loop will keep running as long as the user's guess is NOT equal to the random number.
    while guess != random_number:
        # Ask the user to input a guess.
        # The 'input()' function always returns a string, so we convert it to an integer using int().
        # The 'f-string' (f"") allows dynamic text — it displays the upper limit 'x' in the message.
        guess = int(input(f"Guess a number between 1 and {x}: "))

        # If the guessed number is lower than the random number, give a hint to go higher.
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        
        # If the guessed number is higher than the random number, give a hint to go lower.
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    
    # If the loop exits, it means the user guessed the correct number.
    # The final message congratulates them and shows the correct number.
    print(f'Yay, Congrats! You have guessed the number {random_number}')


# ---------------------- COMPUTER GUESSING FUNCTION ----------------------

# Define another function named 'computer_guess' that also takes one argument 'x'.
# This time, the computer will try to guess a number that YOU (the human) are thinking of.
def computer_guess(x):
    # Set the lowest possible number to 1
    low = 1
    
    # Set the highest possible number to 'x'
    high = x

    # Initialize 'feedback' as an empty string.
    # This variable will store the user's feedback about the computer's guess.
    feedback = ""

    # Continue the loop until the user types 'c', which means the computer guessed correctly.
    while feedback != 'c':
        # If low and high are not the same, generate a random number between them.
        # This simulates the computer "guessing" intelligently within the remaining possible range.
        if low != high:
            guess = random.randint(low, high)
        else:
            # If low == high, there's only one possible number left, so use that.
            guess = low

        # Ask the user for feedback on the computer's guess.
        # The user should type:
        # 'H' if the guess is too high,
        # 'L' if the guess is too low,
        # or 'C' if the guess is correct.
        # The .lower() method converts the input to lowercase to handle both upper and lowercase responses.
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        # If the guess was too high, adjust the upper limit of the range.
        # Since the guess was too high, the actual number must be smaller.
        if feedback == "h":
            high = guess - 1

        # If the guess was too low, adjust the lower limit of the range.
        # Since the guess was too low, the actual number must be greater.
        elif feedback == 'l':
            low = guess + 1

    # Once the loop ends (feedback == 'c'), print a success message.
    # Note: The string should use an f-string to display the actual guessed number.
    # The correct version should be: print(f'Computer guessed your number, {guess}, correctly!')
    print('Computer guessed your number, {guess}, correctly!')


# ---------------------- FUNCTION CALLS ----------------------

# Call the computer_guess() function with 10 as the upper limit.
# That means the user will think of a number between 1 and 10,
# and the computer will try to guess it based on feedback.
computer_guess(10)

# Call the guess() function with 10 as the upper limit.
# Now the human will try to guess the random number the computer has generated between 1 and 10.
guess(10)
