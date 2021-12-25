#สร้างเครื่องประมูลขึ้นมา

print("Welcome to the secret auction program.")

again = True
people = {}
while again:
    name = input("What is your name?: ")
    price = input("What's your bid?: $")
    people[name] = price
    max_price = ""
    max_people = ""
    for bid in people:
        if people[bid] > max_price:
            max_price = people[bid]
            max_people = bid
    Ask = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if Ask == "yes":
        again = True
    else:
        again = False
        print(f"The winner is {max_people} witha a bid of ${max_price}")

# My teacher version

# from replit import clear
# from art import logo
# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()

