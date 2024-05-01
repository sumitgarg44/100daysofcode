#!/usr/bin/env python3

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

# Initialize global variables
player_cards = []
dealer_cards = []

# Predefined Deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(deal,cards_sum):
    if deal:
        while len(dealer_cards) < 2:
            player_cards.append(cards[random.randrange(len(cards))])
            dealer_cards.append(cards[random.randrange(len(cards))])
    else:
        player_cards.append(cards[random.randrange(len(cards))])

        if cards_sum < 17:
            dealer_cards.append(cards[random.randrange(len(cards))])

def sum_of_cards(list_cards,list_cards_sum,player):
    list_cards.sort()
    for list_card in list_cards:
        if list_card == 11 and list_cards_sum > 10 and player:
            list_cards_sum += 1
        else:
            list_cards_sum += list_card
    return list_cards_sum

def find_winner(player_cards,dealer_cards):
    if player_cards > 21:
        print("\nDealer wins!")
    elif player_cards == dealer_cards:
        print("\nIt's a draw!")
    elif player_cards < 21 and dealer_cards > 21:
        print("\nCongratualations! You won.")
    elif player_cards > dealer_cards:
        print("\nCongratualations! You won.")
    else:
        print("\nDealer wins!")

def blackjack():
    # Local variables
    player_cards_sum = 0
    dealer_cards_sum = 0

    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

    if play == "y":
        draw_cards(deal=True,cards_sum=dealer_cards_sum)
        print(f"\nYour's first hand: {player_cards}")
        print(f"Dealer's first hand: {dealer_cards[0]}")

        dealer_cards_sum = sum_of_cards(list_cards=dealer_cards,list_cards_sum=dealer_cards_sum,player=False)

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if another_card == 'y':
            draw_cards(deal=False,cards_sum=dealer_cards_sum)
            dealer_cards_sum += dealer_cards[2]

        player_cards_sum = sum_of_cards(list_cards=player_cards,list_cards_sum=player_cards_sum,player=True)

        print(f"\nYour's final hand: {player_cards}")
        print(f"Dealer's final hand: {dealer_cards}")

        find_winner(player_cards=player_cards_sum,dealer_cards=dealer_cards_sum)

    elif play == "n":
        print("\nGood Bye!")
    else:
        print("\nOops! Invalid choice.")
        blackjack()

blackjack()
