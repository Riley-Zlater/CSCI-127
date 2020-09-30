# --------------------------------------
# CSCI 127, Lab 4
# September 24, 2019
# Riley Slater
# --------------------------------------
# This program displays total points, games played, which season
# and allpossible combination of wins, ties, and losses.
# --------------------------------------


# --------------------------------------
# The Function process_season formats the statistics into a readable format
# and calculates all potential combinations of wins-ties-losses.
# Assuming win = 3, tie = 1, and loss = 0.
# --------------------------------------
# Season - Current season
# Games_played - Total games played for a given season
# Points_earned - Totalpoints earned for a given season
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")

    maxWins = (points_earned // 3)
    ties = 0
    losses = 0

    if not points_earned:
        print ("0-0-" + str(games_played))
    elif points_earned < 3:
        print ("0-" + str(points_earned) + "-0")
    else:
        for wins in range(maxWins, 0, -1):            
            ties = points_earned - wins * 3
            if wins + ties <= games_played:
                losses = games_played - wins - ties
                print ((str(wins)) + "-" + (str(ties)) + "-" + (str(losses)))
                
    print()

# --------------------------------------
# The Function process_seasons formats the statistics from the seasons played.
# --------------------------------------
# Seasons - Statistics from each season.
# --------------------------------------

def process_seasons(seasons):
    for loop in range (len(seasons)):
        process_season(loop + 1, seasons[loop][0], seasons[loop][1])

# --------------------------------------
# The Function main calls the function to start and provides the list of statistics.
# --------------------------------------
# Format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
# --------------------------------------

def main():
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)

# --------------------------------------

main()
