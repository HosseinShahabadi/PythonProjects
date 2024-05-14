import requests
import random
import os
from images import hangman_logo
from images import stages
os.system('cls' if os.name == 'nt' else 'clear')

# Getting a word from mit.edu
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
word = random.choice(words).decode()

# Setup
health = 6
guessed_letters = []
finish = False

print(hangman_logo)
print(f"Health: {health} ============")
print(stages[health])

msg = "Guess the word: "
for num in word:
    msg += "_"
print(msg)

while not finish:
    user_choice = input("enter a letter: ").lower()

    # Checking user input
    if user_choice in guessed_letters:
        msg = "You've already guessed this letter! enter another letter: "
    elif user_choice in word:
        msg = "Well done, enter another letter: "
        guessed_letters.append(user_choice)
    else:
        health -= 1
        msg = "Wrong, enter another letter: "

    for letter in word:
            if letter in guessed_letters:
                msg += letter
            else:
                msg += "_"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(hangman_logo)
    print(f"Health: {health} ============")
    print(stages[health])
    print(msg)

    # Checking conditions
    if len(set(guessed_letters)) >= len(set(word)):
        print("You WON!")
        print(f"The word: {word}")
        finish = True
    if health <= 0:
        print("You Lost!")
        print(f"The word: {word}")
        finish = True
