# -------------------------------
# CSCI 127
# Program 3
# October 08, 2019
# Riley Slater
# Kshithij Mysore
# -------------------------------
# Calculate and display three unique pieces of information
# derived from video_games.csv
# -------------------------------

# -------------------------------
# filter_year shows you the games avaliable
# in a particular year between 2004 and 2008.
# -------------------------------

def filter_year(file_name):
    
    year = int(input("View the releases from a given year enter a year between 2004 and 2008: "))
    
    game_counter = 0
    
    while  year < 2004 or year > 2008:
        year = int(input("Make sure it's between 2004 and 2008: "))
    
    print()
    
    with open(file_name, 'r') as file:
        first_line = file.readline()
        for video_games in file:
            game = video_games.split('"')
            
            if game[31] == str(year):
                game_counter += 1
                print(str(game_counter) + ".", game[1])
    
    file.close()
    print()
    print(game_counter, "games were released in", str(year) + ".\n")
    
# -------------------------------
# filter_platform shows the games avaliable
# for a particular platform.
# -------------------------------    

def filter_platform(file_name):
    
    platforms = []

    with open(file_name, 'r') as file:
        first_line = file.readline()
        for video_games in file:
            games = video_games.split('"')
            
            if games[25] not in platforms:
                platforms.append(games[25])
    print("The Avaliable Platforms")
    print("-----------------------\n")
        
    for loop in range (len(platforms)):
        print(platforms[loop])
        
    print()
        
    user_platform = input("Enter your preferred platform: ")
    
    while user_platform not in platforms:
        user_platform = input("Make sure it's entered exactly as shown above: ")
    
    avaliable_games = []
    
    with open(file_name, 'r') as file2:
        first_line = file2.readline()
        for video_games in file2:
            games = video_games.split('"')
            if games[25] == user_platform:
                avaliable_games.append(games[1])
            
        for loop in range (len(avaliable_games)):
            print(avaliable_games[loop])
    file.close()
    file2.close()
    print()
    print(len(avaliable_games), "games are avaliable on the", user_platform, "platform.\n")
    
# -------------------------------
# filter_statistics calculates and displays
# a variety of statistics from the file.
# -------------------------------
    
def filter_statistics(file_name):
    
    platforms = []
    esrb_rating = []
    single_player_counter = 0
    rating_counter = 0
    total_rating = 0
    average_rating = 0
    
    with open(file_name, 'r') as file:
        first_line = file.readline()
        for video_games in file:
            game = video_games.split('"')
            
            platforms.append(game[25])
            esrb_rating.append(game[27])
            
            if game[5] == '1':
                single_player_counter += 1
                
            if game[25] == platforms[0]:
                total_rating += int(game[19])
                rating_counter += 1
                               
        average_rating = total_rating / rating_counter
        average_rating = round(average_rating, 2)
        
        most_common_esrb_rating = max(set(esrb_rating), key = esrb_rating.count)
        most_used_platform = max(set(platforms), key = platforms.count)
    
    file.close()
    
    print ("The platform with the most games is", most_used_platform)
    print ("The average review score of the games for the", most_used_platform, "is", str(average_rating)+ ".")
    print ("The most common ESRB rating is", most_common_esrb_rating + ".")
    print (single_player_counter, "games are single player.\n")    

# -------------------------------
# main calls each function.
# -------------------------------

def main(file_name):
    filter_year(file_name)
    filter_platform(file_name)
    filter_statistics(file_name)
    
main("video_games.csv")







