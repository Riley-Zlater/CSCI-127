
# --------------------------------------
# CSCI 127
# Practicum 2 - Practice
# Last Edited - October 30, 2019
# Riley Slater
# --------------------------------------
# Question 1 - Any positive value is a win
# and negative values are losses, no ties.
# Calculate the number of wins and losses.
# --------------------------------------

score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

wins = 0
losses = 0

for loop in score_differences.values():
    if loop > 0:
        wins += 1
    else:
        losses += 1

print(wins,"wins -",losses,"loss(es)\n")

# --------------------------------------
# Question 2 - Create the Refrigerator
# subclass that prints the manufacturer
# and cooling agent formatted as so.
# --------------------------------------

class Appliance():
    def __init__ (self, manufacturer):
        self.manufacturer = manufacturer # self = a field, manufacturer = a particular instance

    def get_manufacturer(self):
        return self.manufacturer
        
class Refrigerator(Appliance): # Makes this a subclass of Appliance
    def __init__(self, manufacturer, cooling_agent):
        super().__init__(manufacturer) # INHERIT FIRST!!! Calls the information from the super class
        self.cooling_agent = cooling_agent

    def __str__(self):
        return ("The "+ self.get_manufacturer()+ " refrigerator contains refrigerant "+ self.cooling_agent)


my_refrigerator = Refrigerator("Samsung", "R134a")
print(my_refrigerator)

# --------------------------------------
