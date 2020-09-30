# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:02:51 2019
 CSCI 127 Practicum 2
@author: Riley
"""
def determine_winner(teams):
    best_team = "UNKNOWN"
    most_wins = -1
    for team, wins in teams.items():
        if wins > most_wins:
            best_team = team
            most_wins = wins
    return best_team


nl_east = {}
nl_east["Washington Nationals"] = 93
nl_east["Philadelphia Phillies"] = 81
nl_east["Atlanta Braves"] = 97
nl_east["Miami Marlins"] = 57

nl_west = {}
nl_west["Reds"] = 0

print("NL East Winner:", determine_winner(nl_east))
print("NL West Winner:", determine_winner(nl_west))



class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
           
    def set_record(self, wins, losses):
        self.wins = wins
        self.losses = losses
   
    def __str__(self):
        result = self.name + ": "+ str(self.wins) +" wins and "
        result += str(self.losses)+" losses"
        return result


nationals = Team("Washington Nationals")
nationals.set_record(93, 69)
print(nationals)

astros = Team("Houston Astros")
print(astros)
