import numpy as np

# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data      
# Program 5: Wacky Packages
# Riley Slater      
# Last Modified: November 19, 2019               
# ---------------------------------------------
# Displays all the Wacky Package Cards and their
# appreciated values. Then, it counts how many
# cards we own and updats our list. Lastly, it
# calculates the dollar amount of the cards we own,
# the number of cards we're missing, and the
# dollar amount of our missing cards.
# ---------------------------------------------

class WackyPackageSeries:
    def __init__(self, manufacturer, year, how_many):
        self.manufacturer = manufacturer
        self.year = year
        self.how_many = how_many
        self.cards = np.ndarray(how_many, dtype=WackyPackageCard)


    def __str__(self):
        """__str__ method displays our full arrays of cards"""
        result = "My "+ str(self.year)+ " collection of "+ self.manufacturer+ " Wacky Packages\n"
        result += "\n"
        result += "Number    Description                   Value     Owned\n"
        result += "------    -----------                   -----     -----\n"
        for cards in self.cards:
            result += str(cards) + "\n"
        return result
    
    def read_series_information(self, input_file):
        """reads the information from our file and uses the other class to format it"""
        with open(input_file, 'r') as file:
            index = 0
            for c in file:
                c = c.split(',')
                self.cards[index] = WackyPackageCard(int(c[0]), c[1], float(c[2]))
                index += 1

    def read_collection_information(self, input_file):
        """reads the cards that we own and adds up to the get_cards_owned method"""
        with open(input_file, 'r') as file:
            for cards in file:
                cards = " ".join((cards.lower()).title().split())
                for index in range (0, len(self.cards)):
                    card = self.cards[index]
                    if card.get_description() == cards:
                        card.set_cards_owned(card.get_cards_owned() + 1)

    def collection_value(self):
        """multiplies the values buy the number owned then adds up those numebrs"""
        money = 0.00
        
        for index in (self.cards):           
            money += index.get_value() * index.get_cards_owned()
        
        return money

    def determine_missing_information(self):
        """if our cards owned is zero we add one to the number of missing cards
           and adds the values to our cost missing float"""
        cost_missing = 0.00
        missing = 0
        
        for cards in self.cards:
            if cards.get_cards_owned() == 0:
                cost_missing += cards.get_value()
                missing += 1

        return missing, cost_missing
            
# ---------------------------------------------

class WackyPackageCard:
    def __init__(self, number, description, value):
        self.number = number
        self.description = description
        self.value = value
        self.cards_owned = 0

    def __str__(self):
        return "{:<10d}{:25}{:10.2f}{:10d}".format(self.number, self.description, self.value, self.cards_owned)

    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_cards_owned(self):
        return self.cards_owned

    def set_cards_owned(self, number):
        self.cards_owned = number

# ---------------------------------------------

def main():
    my_collection = WackyPackageSeries("Topps", 1973, 30)
    my_collection.read_series_information("series1.csv")
    print(my_collection)
    my_collection.read_collection_information("mycards.csv")
    print(my_collection)
    print("Value of collection = ${:.2f}".format(my_collection.collection_value()))
    number_of_missing_cards, cost_of_missing_cards = my_collection.determine_missing_information()
    print("Number of missing cards =", number_of_missing_cards)
    print("Cost of purchasing missing cards = ${:.2f}".format(cost_of_missing_cards))
    
# ---------------------------------------------

main()
