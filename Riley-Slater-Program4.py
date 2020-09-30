import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Riley Slater                          |
# Last Modified: October 25, 2019       |
# ---------------------------------------
# This program provides different information
# derived from the pokedex file.
# ---------------------------------------

# ---------------------------------------
# The Class Pokemon is for extracting specific
# information from the pokedex.
# ---------------------------------------

class Pokemon:
    
# The __init__ method provides the variable(pokemon instead of self)
# , name, rank, combat level, and type of each pokemon.
    def __init__(self, name, rank, combat, element):
        self.name = name
        self.rank = rank
        self.combat = combat
        self.element = element

# The get_name method returns each pokemon name
# from the file.
    def get_name(self):
        return self.name
    
# The method get_rank returns the rank of each
# pokemon from the file.
    def get_rank(self):
        return self.rank
    
# The method get_combat returns the combat
# level of each pokemon from the file.
    def get_combat(self):
        return self.combat
    
# The method get_type returns the element
# type of each pokemon.
    def get_type(self):
        return self.element
    
# The method __str__ fromats the rank, name,
# combat level, and element types as desired
# for later use.
    def __str__(self):
        return "Number: "+ str(self.get_rank())+ ", Name: "+ self.get_name().capitalize()+ ", CP: "+ str(self.get_combat())+ ": Type: "+ ' and '.join(self.get_type())
    
# ---------------------------------------
# The function print_pokedex loops through 
# the pokedex and uses the __str__ method 
# displayed as pokemon to produce the altered
# formatting of the original file in a more 
# digestable version.
# ---------------------------------------

def print_pokedex(pokedex):
    print()
    print("The Pokedex")
    print("-----------")
    
    for pokemon in pokedex:
        print(pokemon)

# ---------------------------------------
# The lookup_by_name function asks if the
# inputted name is one of the names returned
# from the get_name method. If not the for
# loop breaks and it prints that there is
# no Pokemon named that.
# ---------------------------------------

def lookup_by_name(pokedex, name):
    
    for pokemon in pokedex:
        if name == pokemon.get_name():
            print(pokemon)
            break
    else:
        print("There is no Pokemon named", name)

# ---------------------------------------
# The lookup_by_number function operates 
# the same as lookup_by_name only this
# function uses the values returned from
# the get_rank method.
# ---------------------------------------

def lookup_by_number(pokedex, number):

    for pokemon in pokedex:           
        if number == pokemon.get_rank():
            print(pokemon)
            break
    else:
        print("There is no Pokemon number", number)

# ---------------------------------------
# The total_by_type function calculates how
# many pokemon have a certain type. It does
# this by checking if that type is returned
# by the get_type method. If it is the
# counter increases by one, otherwise
# it doesn't increase. (Included to work
# with multiple types such as if you input
# normal and flying the result should be 5
# as 5 pokemon have both normal and flying.)
# ---------------------------------------

def total_by_type(pokedex, pokemon_type):
    type_counter = 0
    
    for pokemon in pokedex:
        if pokemon_type in pokemon.get_type():
            type_counter += 1

    print("Number of Pokemon that contain type", pokemon_type, "=", type_counter)

# ---------------------------------------
# The average_hit_points function adds all
# the combat levels then divides by the
# number of pokemon to produce the average.
# ---------------------------------------

def average_hit_points(pokedex):
    hit_point_counter = 0
    
    for pokemon in pokedex:
        hit_point_counter += pokemon.get_combat()
        
    average = round((hit_point_counter/ len(pokedex)), 2)        
    print("Average Pokemon combat points =", average)

# ---------------------------------------
# The print_menu function simply prints
# all of the menu options for the user.
# ---------------------------------------
    
def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit\n")

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
