#==================== Our Blackjack House Rules ====================#

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have an equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

#===================================================================#

import os
import random

logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''

def is_float(element: any):
    '''Check if an element is float'''
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False

def print_cards(cards):
    msg = ""
    counter = 0
    for card in cards:
        msg += str(card)
        counter += 1
        if counter < len(cards):
            msg += ", "
    return msg

def total_cards_point(cards):
    point = 0
    counter = 0
    for card in cards:
        point += card
        if card == 11:
            counter += 1
    
    # Checking cards for Aces if total point is more than 21
    while point > 21:
        if counter > 0:
            point -= 10
            counter -= 1
        else:
            break
    return point

def get_player_choice():
    player_choice = input('Type "hit" for another card, or "stand" to skip: ').lower()
    while not (player_choice == 'hit' or player_choice == 'stand'):
        player_choice = input('Please enter a valid input, type "hit" for another card, or "stand" to skip: ').lower()
    return player_choice

# If the total points of your cards exceed 21, then you will lose the game.
def check_bust(cards):
    point = total_cards_point(cards)
    if point > 21:
        return True
    else:
        return False

# If you receive an Ace and a card with a value of 10, you will win.
def check_blackjack(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return True
    else:
        return False

# Main function
def blackjack():
    # First 2 cards
    for i in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    # Revealing player's cards and the dealer's first card.
    print(f"The Dealer's card is {dealer_cards[0]}")
    print(f"Your cards are {print_cards(player_cards)} or {total_cards_point(player_cards)}")

    # This function checks whether the player has a blackjack.
    if check_blackjack(dealer_cards) and check_blackjack(player_cards):
        print(f"----- Blackjack for the Player & the dealer! -----")
        return 'push'
    if check_blackjack(player_cards):
        print(f"----- Blackjack for the Player! -----")
        return 'win'

    print("Player's Turn --------------------")
    player_choice = get_player_choice()
    while player_choice == 'hit':
        player_cards.append(random.choice(cards))
        print(f"You got {player_cards[-1]}")
        print(f"Your cards are {print_cards(player_cards)} or {total_cards_point(player_cards)}")
        if check_bust(player_cards):
            print("----- Player Bust! -----")
            return 'lose'
        else:
            player_choice = get_player_choice()

    print("Dealer's Turn --------------------")
    print(f"The Dealer's cards are {print_cards(dealer_cards)} or {total_cards_point(dealer_cards)}")
    if check_blackjack(dealer_cards):
        print(f"----- Blackjack for the Dealer! -----")
        return 'lose'
    while total_cards_point(dealer_cards) < 17:
        print("Dealer need more points.")
        dealer_cards.append(random.choice(cards))
        print(f"Dealer got {dealer_cards[-1]}")
        print(f"The Dealer's cards are {print_cards(dealer_cards)} or {total_cards_point(dealer_cards)}")
        if check_bust(dealer_cards):
            print("----- Dealer Bust! -----")
            return 'win'

    print("=============== Checking results ===============")
    dealer_point = total_cards_point(dealer_cards)
    player_point = total_cards_point(player_cards)
    print(f"Your cards are {print_cards(player_cards)} or {player_point}")
    print(f"The Dealer's cards are {print_cards(dealer_cards)} or {dealer_point}")
    if dealer_point == player_point:
        print("Draw!")
        return 'draw'
    elif dealer_point > player_point:
        print("Dealer wins!")
        return 'lose'
    else:
        print("Player wins!")
        return 'win'

# Start of sequence programming ====================

#       Ace  2  3  4  5  6  7  8  9  10   J   Q   K
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards = []
player_cards = []

os.system('cls' if os.name == 'nt' else 'clear')
print(logo)

balance = input("What's your initial balance: $")
while not is_float(balance):
    balance = input("Wrong input, What's your initial balance: $")
balance = float(balance)
# Later, we can add a service here that allows for direct money transfers.
print(f"An amount of ${balance} has been withdrawn from your bank account.")

bet_amount = input(f"Your balance is {balance}, what's your bet: $")
while (not is_float(bet_amount)) or float(bet_amount) > balance:
    bet_amount = input("Wrong input, What's your bet: $")
bet_amount = float(bet_amount)

while 1:
    result = blackjack()
    print("---------- Round ends ----------")
    if result == 'win':
        print(f"You won ${bet_amount}")
        balance += bet_amount
    elif result == 'lose':
        print(f"You lost ${bet_amount}")
        balance -= bet_amount
    
    dealer_cards = []
    player_cards = []

    if balance == 0:
        print("===== Insufficient balance! =====")
        print("===== Thanks for choosing us ====")
        break

    print(f"Your balance is {balance}")
    user_choice = input("Do you want to coninue? (Y/N)").lower()
    if user_choice == 'y' or user_choice == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"Your balance is {balance}")
        bet_amount = input(f"What's your bet: $")
        while (not is_float(bet_amount)) or float(bet_amount) > balance:
            bet_amount = input("Wrong input, What's your bet: $")
        bet_amount = float(bet_amount)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"${balance} added to your bank account")
        print("===== Thanks for choosing us ====")
        break
