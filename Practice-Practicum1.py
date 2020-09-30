# -------------------------------
# Riley Slater
# Practice for Practicum One
# 01 October 2019
# -------------------------------

# Practice Question One

"""
def create_list(how_many):
    
    result = []
    for loop in range(how_many):
       result.append(loop + 1)
    return result

how_many = int(input("Enter the number of integers the list should contain: "))
numbers = create_list(how_many)
print(numbers)
"""

# Practicce Question Two

"""
def pokemon_battle(my_pokemon):

    winner = ""
    power_rating = 0
    placement = 0

    if not my_pokemon:
        winner = "Nobody"
    
    for loop in range(len(my_pokemon)):

        if power_rating < my_pokemon[loop][1]:
            power_rating = my_pokemon[loop][1]
            placement = loop

        winner = my_pokemon[placement][0]
    
        
    print ("The winner is", winner)



pokemon_battle([["Bulbusaur", 132],["Squirtle", 175],["Pikachu", 75]])
pokemon_battle([])
pokemon_battle([["Rattata", 60],["pidgey", 55]])
pokemon_battle([["Rattata", 60],["Pidgey", 55],["Ekans", 60]])
"""
