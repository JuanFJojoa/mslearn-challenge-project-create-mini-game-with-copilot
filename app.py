#make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move

#make the game a best of three


import random


#create a function to get the user's choice put the user's choice in lowercase

def get_user_choice():
  user_input = input("Enter your choice (rock/paper/scissors):").lower()
  if user_input in ["rock", "paper", "scissors"]:
    return user_input
  else:
    print("Invalid input. Please try again.")
    return get_user_choice()

#function to get the computer's choice
def get_computer_choice():
  computer_input = random.choice(["rock", "paper", "scissors"])
  return computer_input

#function to determine the winner
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  elif user_choice == "rock" and computer_choice == "paper":
    return "Computer won!"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "You won!"
  elif user_choice == "paper" and computer_choice == "rock":
    return "You won!"
  elif user_choice == "paper" and computer_choice == "scissors":
    return "Computer won!"
  elif user_choice == "scissors" and computer_choice == "rock":
    return "Computer won!"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "You won!"
  else:
    return "Invalid input. Please try again."
  

  #function to start the game and ask the user if they want to play aga
def play_RPS():
  
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(user_choice)
    print(computer_choice)
    print(determine_winner(user_choice, computer_choice))
    play_again = input("Would you like to play again? (y/n)").lower()
    if play_again == "y":
        play_RPS()
    else:
        print("Thanks for playing!")

play_RPS()


