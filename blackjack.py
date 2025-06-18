#!/usr/bin/env python3

import random
from helpers.clear_screen import clear_screen
from static.arts import black_jack

def draw_cards():
    # Predefined Deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

def calculate_score(cards):
    # BlackJack
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def find_winner(user_score,computer_score):
    if user_score == computer_score:
        return("\nIt's a draw!")
    elif computer_score == 0:
        return("\nLose, Dealer has a BlackJack.")
    elif user_score == 0:
        return("\nCongratualations! You have a BlackJack.")
    elif user_score > 21:
        return("\nDealer wins!")
    elif computer_score > 21:
        return("\nCongratualations! You won.")
    elif user_score > computer_score:
        return("\nCongratualations! You won.")
    else:
        return("\nDealer wins!")

def blackjack():
    player_cards = []
    dealer_cards = []
    is_game_over = False

    print(black_jack.logo)

    for _ in range(2):
        player_cards.append(draw_cards())
        dealer_cards.append(draw_cards())

    while not is_game_over:
        print(f"\nYour's hand: {player_cards}")
        print(f"Dealer's hand: {dealer_cards[0]}")
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y':
                player_cards.append(draw_cards())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(draw_cards())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nYour's final hand: {player_cards}")
    print(f"Dealer's final hand: {dealer_cards}")

    print(find_winner(user_score=player_score,computer_score=dealer_score))

def continue_play():
    want_to_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

    if want_to_play == "y":
        clear_screen()
        blackjack()
    elif want_to_play == "n":
        print("\nGood Bye!")
    else:
        print("\nOops! Invalid choice.")
        continue_play()

continue_play()
