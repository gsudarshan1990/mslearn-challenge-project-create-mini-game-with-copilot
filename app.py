
"""
Create a simple Rock, Paper, Scissors game in Python. The program should:

1. Prompt the user to choose rock, paper, or scissors.
2. Have the computer randomly select one of the three options.
3. Compare both choices and determine the winner using these rules:
   - Rock beats scissors.
   - Scissors beat paper.
   - Paper beats rock.
4. Print both choices and announce the winner.
5. With the prompt as "screen" inform the option as invalid
5. Optionally, loop the game and allow the user to play again until they choose to quit.
"""
import random
def get_user_choice():
    user_input = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_input in ['rock', 'paper', 'scissors']:
        return user_input
    elif user_input == 'quit':
        return None
    else:
        print("Invalid option. Please try again.")
        return get_user_choice()