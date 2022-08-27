import random
from traceback import print_tb
print("***Welcome to Rock, Paper and Scissor Game***")
Rock = "1"
Paper = "2"
Scissor = "3"
player_choice = int(input("What is your choice? Type:1 2 or 3 "))
computer_choice = random.randint(1,3)
print(f"Computer chooses: {computer_choice}")
if player_choice == computer_choice:
    print("Match draw!!")
elif player_choice == 1 and computer_choice == 2:
    print("You lost!! Paper hides Rock.")
elif player_choice == 1 and computer_choice == 3:
    print("You won!! Rock kills scissor.") 
elif player_choice == 2 and computer_choice == 1:
    print("You won!! Paper hides rock.")
elif player_choice == 2 and computer_choice == 3:  
    print("You lost!! Scissor cuts the paper.")
elif player_choice == 3 and computer_choice == 1:
    print("You lost!! Rock kills scissor. ")
elif player_choice == 3 and computer_choice == 2:
    print("You won!! Scissor cuts the paper.")  
else:
    print("You lost, you typed a invalid number.")                      
