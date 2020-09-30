# ---------------
# My Solutions
# ---------------
"""
def grocery_bill(file_name):

    file = open(file_name, "r")

    cost = 0
    
    for price in file:
        cost += float(price)

    cost = round(cost, 2)
    
    print(cost, "Dollars")

grocery_bill("town_and_country.in")


def general_flush(cards):
    suits = []
    for suit in cards:
        suits.append(suit[1])

    check_suit = suits.count(suits[0])

    if check_suit == len(cards):
        return True
    else:
         return False


general_flush([[3, "hearts"]])
general_flush([[3, "hearts"], [9, "hearts"], [6, "hearts"]])
general_flush([[3, "hearts"], [9, "spades"]])
"""

# -------------------
# In Class Solutions
# -------------------
"""
def general_flush(cards):
    for card in cards:
        if card[1] != cards[0][1]:
            return False
    
    return True

def general_flush(cards):
    suits = []
    for card in cards:
        suits.append(card[1])

    return suits.count(suits[0]) == len(cards)
    
print(general_flush([[3, "hearts"]]))
print(general_flush([[3, "hearts"], [9, "hearts"], [6, "hearts"]]))
print(general_flush([[3, "hearts"], [2, "diamonds"], [9, "spades"]]))


def grocery_bill(file_name):

    total = 0.0
    
    with open(file_name, 'r') as file:
        
        for line in file:
            total += float(line)

        print("The total bill equals - ${:.2f}".format(total))

        file.close()


grocery_bill("town_and_country.in")
"""








