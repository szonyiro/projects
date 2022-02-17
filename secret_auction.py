from replit import clear

bidders = {}


def inputs():
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    bidders[name] = bid
    return


def winning_bid():
    winner = max(bidders, key=bidders.get)
    print(f"The winner is {winner} with a bid of £{bidders[winner]}")
    return


while True:
    inputs()
    repeat = input("\nAre there any other bidders? Type 'yes' or 'no'")
    clear()
    if repeat == "no":
        break

winning_bid()
