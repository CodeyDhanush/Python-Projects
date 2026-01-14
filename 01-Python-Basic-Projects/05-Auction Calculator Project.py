print("*****WELCOME TO AUCTION CALCULATOR*****")
def highest_bidder():
    max_key = max(auction_data, key=auction_data.get)
    max_value = auction_data[max_key]

    print(f"The winner is {max_key} with a bid of ${max_value}")

auction_data = {}
continue_bidding = True
while continue_bidding:
    name = input("what is your name?:" )
    price = int(input("What is your bid?:"))
    auction_data.update({name: price})
    print(auction_data)
    next_bidder = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if next_bidder == "yes":
        continue_bidding = True

    elif next_bidder == "no":
        continue_bidding = False
        highest_bidder()
