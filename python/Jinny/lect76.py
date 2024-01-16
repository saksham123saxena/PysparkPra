# it is the empty dictionary
import os


def find_winner(bidder_details):
    highest = 0
    winner = ''
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest:
            highest = bidding_price
            winner = bidder
    print(f"Winner : {winner} and his bid is : {highest}")



bidder_data = {}
flag = True
while flag:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bidder_data[name] = price
    more_bidders = input("are there are more bidders ? Tye 'yes' or 'no' : ").lower()
    if more_bidders == 'no':
        flag = False
        find_winner(bidder_data)
    elif more_bidders == 'yes':
        os.system('clear')
