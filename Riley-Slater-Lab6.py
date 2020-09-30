# --------------------------------------
# CSCI 127, Lab 6                      |
# October 6, 2019                      |
# Riley Slater                         |
# --------------------------------------

# --------------------------------------
# count_earthquakes: counts the number of earthquakes between two given numbers.
# --------------------------------------

def count_earthquakes(file_name, low_bound, high_bound):
    
    counter = 0
    
    with open(file_name, 'r') as file:
        first_line = file.readline()
        for earthquake in file:
            separation = earthquake.split(',')
            if float(separation[2]) >= low_bound and float(separation[2]) <= high_bound:
                counter += 1

        return counter
    
# -----------------------------------
# earthquake_locations: formats all earthquakes and removes duplicates.
# -----------------------------------


def earthquake_locations(file_name):
    
    separation = []
    locations = []
    counter = 0
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    with open(file_name, 'r') as file:
        first_line = file.readline()
        for earthquakes in file:
            separation = earthquakes.split(',')
            for loop in separation:
                if loop[0] in letters:
                    locations.append(loop)
                    
    location = list(set(locations))
    location.sort()
    
  
    print('Alphabetical Order of Earthquake Locations')
    print('------------------------------------------')
    for places in location:
        counter += 1
        print (str(counter) + '.', places)
    print()

# -------------------------------------
# average_magnitude: finds the average magnitude for all earthquakes.
# -------------------------------------


def average_magnitude(file_name):

    total_magnitude = 0
    number_of_earthquakes = 0
    
    with open(file_name, 'r') as file:
        first_line = file.readline()
        for earthquake in file:
            number_of_earthquakes += 1
            separation = earthquake.split(',')
            total_magnitude += float(separation[2])
            
        average_magnitude = total_magnitude / number_of_earthquakes 
        return(average_magnitude)

# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(file_name)
    
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
