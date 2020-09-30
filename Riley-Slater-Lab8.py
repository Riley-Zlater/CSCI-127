
# -----------------------------------------------------
# CSCI 127, Lab 8
# October 22, 2019
# Riley Slater
# -----------------------------------------------------

class Contact:
    """Contact class for reprsenting and manipulating a list of contacts"""

    def __init__(person, first, last, number):
        """A constructor method that sets the first name, last name
           and phone number"""
        person.first = first
        person.last = last
        person.number = number

    def print_entry(person):
        """A reader method that calculates the formatting and prints
           the first name, last name, and phone number when called"""
        formatting = 35 - (len(person.first) + len(person.last))
        print(person.first, person.last, person.number.rjust(formatting))

    def set_first_name(person, first):
        """A writer method that changes the first, first name"""
        person.first = first

    def set_title(person, first):
        """A writer method that adds the title before the first name"""
        person.first = first + " " + person.first

    def get_cell_number(person):
        """A reader method that returns the first phone number"""
        return(person.number)

    def get_area_code(person):
        """A reader method that returns the first three digits 
           of the first phone number"""
        return(person.number[:3])

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
