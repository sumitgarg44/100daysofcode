import os
from static.arts import auction_art

print(f"{auction_art.logo}\n\nWelcome to the secret auction program.")

bids = {}
is_continue = True

def highest_bid(bids_dict):
    highest_bid = 0
    winner = ""
    for bidder in bids_dict:
        if float(bids_dict[bidder]) > highest_bid:
            highest_bid = float(bids[bidder])
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")
    

while is_continue:
    bidder = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bids[bidder] = bid

    another_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if another_bid == "no":
        is_continue = False
        highest_bid(bids)
    else:
        is_continue = True
        os.system('clear')

