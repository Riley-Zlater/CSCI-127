

# -----------------------------------------+
# Riley Slater                             |
# CSCI 127, Program 2                      |
# Last Updated: 28 Spetember 2019          |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+

def get_all_ranks(hand):
    
    result = []
    for card in hand:
        result.append(card[0])
    return result

def royal_flush(hand):


    suits = []          # Separates the suits from the ranks
    for card in hand:
        suits.append(card[1])
    
    total_card_count = hand[0][0] + hand[1][0] + hand[2][0] + hand[3][0] + hand[4][0]       # Adds all five the ranks together
    
    check_suit = suits.count(suits[0])      # Counts how many times the first suit appears in the suits list
    
    if check_suit == 5 and total_card_count == 60:      # All five cards must have the same suit and the ranks must add to 60
        return True
    else:
        return False

def straight_flush(hand):
    
    suits = []          # Separates the suits from the ranks
    for card in hand:
        suits.append(card[1])

    ranks = []          # Separates the ranks from the suits
    for card in hand:
        ranks.append(card[0])

    check_suit = suits.count(suits[0])      # Counts how many times the first suit appears in the suits list

    for loop in range (len(hand)):
        if ranks[loop] != 14 and check_suit == 5 and ranks[loop] + 1 == ranks[loop + 1]:      # All suits must be the same, the ranks must be in ascending
            return True                                                                       # consecutive order, and the rank 14 cannot appear
        else:
            return False

def straight(hand):

    ranks = []          # Separates the ranks from the suits
    for card in hand:
        ranks.append(card[0])

    for loop in range (len(hand)):
        if ranks[loop] + 1 == ranks[loop + 1]:      # The ranks must be in asceding consecutive order
            return True
        else:
            return False

def four_of_a_kind(ranks):
    
    frequent_element = max(set(ranks), key = ranks.count)       # Finds the most often occurring element in the list

    if ranks.count(frequent_element) == 4:      # The most often occurring element must appear 4 times
        return True
    else:
        return False

def full_house(ranks):

    frequent_element = max(set(ranks), key = ranks.count)       # Finds the most often occurring element in the list

    ranks2 = ranks[:]       # Copies the list

    while frequent_element in ranks2:       # Removes the most often occurring element from the copied list
        ranks2.remove(frequent_element)

    if ranks.count(frequent_element) == 3 and ranks2[0] == ranks2[1]:       # The most often occurring element must appear 3 times
        return True                                                         # and the two elements left over in the second list must be the same
    else:
        return False

def three_of_a_kind(ranks):

    frequent_element = max(set(ranks), key = ranks.count)       # Finds the most often occurring element in the list

    if ranks.count(frequent_element) == 3:      # The most often occurring element must appear 3 times
        return True
    else:
        return False

def two_pair(ranks):

    frequent_element = max(set(ranks), key = ranks.count)       # Finds the most often occurring element in the list

    ranks2 = ranks[:]       # Copies the list

    while frequent_element in ranks2:       # Removes the most often occurring element from the copied list
        ranks2.remove(frequent_element)

    frequent_element2 = max(set(ranks2), key = ranks2.count)        # Finds the most often occurring element in the copied list
                                                                    # post the removal of the previously most often occurring element

    if ranks.count(frequent_element) == 2 and ranks.count(frequent_element2) == 2:      # Both most often occurring elements must appear twice
        return True
    else:
        return False

def one_pair(ranks):

    frequent_element = max(set(ranks), key = ranks.count)       # Finds the most often occurring element in the list

    if ranks.count(frequent_element) == 2:      # The most common occurring element must appear twice
        return True
    else:
        return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[11, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing


    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")

    evaluate([[14, "spades"], [10, "spades"], [8, "spades"], [2, "hearts"], [5, "spades"]])     # nothing
    evaluate([[14, "spades"], [6, "spades"], [8, "spades"], [6, "hearts"], [5, "spades"]])      # 1 pair
    evaluate([[14, "spades"], [6, "spades"], [14, "clubs"], [6, "hearts"], [5, "spades"]])      # 2 pair
    evaluate([[14, "spades"], [6, "spades"], [8, "spades"], [6, "hearts"], [6, "clubs"]])       # 3 of a kind
    evaluate([[3, "spades"], [5, "spades"], [6, "spades"], [4, "hearts"], [2, "spades"]])       # straight
    evaluate([[4, "spades"], [6, "spades"], [4, "diamonds"], [6, "hearts"], [6, "clubs"]])      # full house
    evaluate([[14, "spades"], [6, "spades"], [6, "diamonds"], [6, "hearts"], [6, "clubs"]])     # 4 of a kind
    evaluate([[13, "spades"], [11, "spades"], [12, "spades"], [9, "spades"], [10, "spades"]])   # straight flush
    evaluate([[13, "spades"], [11, "spades"], [12, "spades"], [14, "spades"], [10, "spades"]])  # royal flush

# -----------------------------------------+

main()
