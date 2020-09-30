import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# November 19, 2019                               |
# Riley Slater                                    |
# -------------------------------------------------

def read_file(file_name):
    field = []
    students = []
    
    with open(file_name, 'r') as file:
        first_line = file.readline()
        for statistics in file:
            stat = statistics.split(',')
            if stat[0] not in field:
                field.append(stat[0])
            if stat[1] not in students:
                students.append(int(stat[1][:-1]))

    return np.array(field), np.array(students)

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)

    x = college_names
    y = college_enrollments
    colors = ['blue', 'gold', 'blue', 'gold', 'blue', 'gold', 'blue']
    
    plt.title('Montana State University Fall 2019 Enrollment')
    plt.xlabel('College Name')
    plt.ylabel('College Enrollment')
    
    plt.yticks(np.arange(0, 4500, 400))    
    plt.ylim(0, 4500)
    
    plt.bar(x, height=y, color=colors)
    plt.show()

# -------------------------------------------------

main("fall-2019.csv")
