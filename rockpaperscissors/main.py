import random  
# The 'random' module is imported so that the computer can make random choices (rock, paper, or scissors).
# Without this module, the computer would not be able to "play" unpredictably.


def play():  
    # Define a function called 'play'. This function handles one full round of the game
    # — getting the user’s input, generating the computer’s move, and deciding who wins.

    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n  ")  
    # The 'input()' function displays a message to the user and waits for them to type something.
    # The entered value is stored in the variable 'user'.
    # The player must type either:
    #   'r' → for rock
    #   'p' → for paper
    #   's' → for scissors

    computer = random.choice(['r', 'p', 's'])  
    # 'random.choice(sequence)' randomly selects one item from a list.
    # Here, the list ['r', 'p', 's'] represents the three possible choices for the computer.
    # The chosen value ('r', 'p', or 's') is stored in the variable 'computer'.

    if user == computer:  
        # This 'if' condition checks if both the player and computer made the same choice.
        # Example: if both chose 'r', then it's a tie.
        return "It's a tie!"  
        # The 'return' statement ends the function and gives this message back to whoever called 'play()'.

    if is_win(user, computer):  
        # This 'if' statement calls the helper function 'is_win()' to check if the player beat the computer.
        # The function will return True if the player wins, or None/False if not.
        return 'You Won!'  
        # If 'is_win()' returns True, this line executes and tells the player they won.

    return 'You Lost!'  
    # If neither of the above conditions are true,
    # that means the computer must have won, so this message is returned.


def is_win(player, opponent):  
    # Define a helper function called 'is_win' that takes two arguments:
    # 'player' → represents the human’s move.
    # 'opponent' → represents the computer’s move.
    # This function checks all the possible winning conditions for the player.

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):  
        # This single 'if' statement uses logical 'or' to check all possible win cases:
        # 1. Rock ('r') beats Scissors ('s')
        # 2. Scissors ('s') beats Paper ('p')
        # 3. Paper ('p') beats Rock ('r')
        # If any of these are true, it means the player has won the round.
        return True  
        # Returns True to indicate that the player has won.
        # Otherwise, the function implicitly returns None (meaning player didn’t win).


print(play())  
# Calls the 'play()' function, which starts the game.
# It prints the returned message (either "You Won!", "You Lost!", or "It's a tie!") to the console.
