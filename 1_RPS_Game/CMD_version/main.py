import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [Rock, Paper, Scissors]
hand = ["Rock", "Paper", "Scissors"]

# Getting user choice.
user_choice = input("Welcome to RPS. Type 0 for Rock, 1 for Paper and 2 for Scissors: ")

# Checking user input.
if user_choice.isdigit() and (int(user_choice) <= 2 and int(user_choice) >= 0):
    user_choice = int(user_choice)
else:
    print("ERROR, you typed an invalid number!")
    quit()

# Generating computer choice.
computer_choice = random.randint(0, 2)

print(f"You chose {hand[user_choice]}:")
print(game_images[user_choice])

print(f"Computer chose {hand[computer_choice]}.")
print(game_images[computer_choice])
    
# Calculating the result.
if user_choice == 0:
    if computer_choice == 0:
        print("Draw!")
    elif computer_choice == 1:
        print("You Lose!")
    else:
        print("You Win!")
elif user_choice == 1:
    if computer_choice == 1:
        print("Draw!")
    elif computer_choice == 2:
        print("You Lose!")
    else:
        print("You Win!")
elif user_choice == 2:
    if computer_choice == 2:
        print("Draw!")
    elif computer_choice == 0:
        print("You Lose!")
    else:
        print("You Win!")
else:
    print("ERROR!")
