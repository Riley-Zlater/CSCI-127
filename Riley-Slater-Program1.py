# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: Liberty Bell Slot Machine
# Riley Slater
# Last Modified:14/9/19
# ---------------------------------------
# Simulate a modified Liberty Bell Slot Machine.
# ---------------------------------------

import random

# Constants that represent the result of spinning a reel
DIAMOND = 1     
HEART = 2
SPADE = 3
HORSESHOE = 4
LIBERTY_BELL = 5

# ---------------------------------------
# spin_payout
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Returns an integer, the payout of the spin
# ---------------------------------------

def spin_payout(reel_1, reel_2, reel_3):
    if reel_1 + reel_2 + reel_3 == 15:
        return(50)
    elif reel_1 == HEART and reel_2 == HEART and reel_3 == HEART:
        return(40)
    elif reel_1 + reel_2 + reel_3 == 3:
        return(30)
    elif reel_1 == SPADE and reel_2 == SPADE and reel_3 == SPADE:
        return(20)
    elif reel_1 == HORSESHOE and reel_2 == HORSESHOE and reel_3 == HORSESHOE:
        return(10)
    elif reel_1 == HORSESHOE and reel_2 == HORSESHOE or reel_2 == HORSESHOE and reel_3 == HORSESHOE or reel_1 == HORSESHOE and reel_3 == HORSESHOE:
        return(5)
    else:
        return(0)
    

# ---------------------------------------
# convert
# ---------------------------------------
# reel: the symbol on a reel, an integer constant
# ---------------------------------------
# Returns a string, the printing value of integer
# ---------------------------------------

def convert(reel):
    if reel == DIAMOND:
        return "diamond"
    elif reel == HEART:
        return "heart"
    elif reel == SPADE:
        return "spade"
    elif reel == HORSESHOE:
        return "horseshoe"
    elif reel == LIBERTY_BELL:
        return "bell"
    else:
        return "error!"

# ---------------------------------------
# test_known_spin
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Display a message that shows the spin and its payout
# ---------------------------------------

def test_known_spin(reel_1, reel_2, reel_3):
    message = "{:10}".format(convert(reel_1))
    message += "{:10}".format(convert(reel_2))
    message += "{:10}".format(convert(reel_3))
    message += "{:-6d}".format(spin_payout(reel_1, reel_2, reel_3))
    print(message)

# ---------------------------------------
# test_known_spins
# ---------------------------------------
# For testing purposes, evaluate a variety of known spins
# ---------------------------------------

def test_known_spins():
    print("{:10}{:10}{:10}{}".format("REEL 1", "REEL 2", "REEL 3", "PAYOUT"))
    print("{:10}{:10}{:10}{}".format("------", "------", "------", "------"))
    test_known_spin(LIBERTY_BELL, LIBERTY_BELL, LIBERTY_BELL)
    test_known_spin(HEART, HEART, HEART)
    test_known_spin(DIAMOND, DIAMOND, DIAMOND)
    test_known_spin(SPADE, SPADE, SPADE)
    test_known_spin(HORSESHOE, HORSESHOE, HORSESHOE)
    test_known_spin(HORSESHOE, HORSESHOE, HEART)
    test_known_spin(HORSESHOE, DIAMOND, HORSESHOE)
    test_known_spin(SPADE, HORSESHOE, HORSESHOE)
    test_known_spin(HEART, HEART, HORSESHOE)
    test_known_spin(LIBERTY_BELL, DIAMOND, SPADE)

# ---------------------------------------
# simulate
# ---------------------------------------
# how_many: the number of spins to take, an integer
# ---------------------------------------
# Simulate the Liberty Bell Slot Machine being played
# how_many times.  Calculate and print the expected winnings.
# ---------------------------------------

def simulate(how_many):
    total_payout = 0
    per_dollar = 0
    potential_outcomes = [DIAMOND, HEART, SPADE, HORSESHOE, LIBERTY_BELL]
    for loop in range(how_many):
        reel_1 = random.choice(potential_outcomes)
        reel_2 = random.choice(potential_outcomes)
        reel_3 = random.choice(potential_outcomes)
        total_payout += spin_payout(reel_1, reel_2, reel_3)
    per_dollar = total_payout / (how_many / 20)
    per_dollar *= .01
    per_dollar = round(per_dollar, 2)
    print("For every $1.00 spent, you can expect to win", per_dollar, "dollar(s) back.")

##----------------------------------------
## This allows you to view the randomized spins from the simulation.
## To run properly comment out the above code and uncomment the code below.
## Added this for fun. :)
##----------------------------------------
"""
def simulate(how_many):    
    print("{:10}{:10}{:10}{}".format("REEL 1", "REEL 2", "REEL 3", "PAYOUT"))
    print("{:10}{:10}{:10}{}".format("------", "------", "------", "------"))
    Potential_Outcomes = [DIAMOND, HEART, SPADE, HORSESHOE, LIBERTY_BELL]
    for loop in range(how_many):
        reel_1 = random.choice(Potential_Outcomes)
        reel_2 = random.choice(Potential_Outcomes)
        reel_3 = random.choice(Potential_Outcomes)
        winnings = spin_payout(reel_1, reel_2, reel_3)
        spins = "{:10}".format(convert(reel_1))
        spins += "{:10}".format(convert(reel_2))
        spins += "{:10}".format(convert(reel_3))
        spins += "{:-6d}".format(winnings)
        print(spins)
"""            
# ---------------------------------------
# main - controls the main flow of logic
# ---------------------------------------

def main():
    print("Program 1: Liberty Bell Slot Machine Simulation\n")
    print("--> Part 1: Testing Known Spins\n")
    test_known_spins()
    print("\n--> Part 2: Simulating 500,000 Spins\n")
    simulate(500000)
          
# ---------------------------------------

main()
