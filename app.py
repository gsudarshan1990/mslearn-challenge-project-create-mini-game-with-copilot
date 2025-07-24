
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

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
    
    def get_user_choice(self):
        while True:
            user_input = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
            if user_input in self.choices:
                return user_input
            elif user_input == 'quit':
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid choice. Please try again.")
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "Computer wins!"
    
    def play_game(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
