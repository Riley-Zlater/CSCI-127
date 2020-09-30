"""
import pandas as pd

units = ["Chemical and Biological Engineering", "Civil Engineering", "Computer Engineering", "General Engineering", "Mechanical and INdustrial Engineering", "School of Computing"]
enrollments = [563, 731, 410, 210, 1463, 552]

dataset = list(zip(units, enrollments))
dataframe = pd.DataFrame(data=dataset, columns=["Unit", "Enrollment"])

dataframe = dataframe.drop([1,2,3,4])
dataframe = dataframe.iloc[::-1]
print(dataframe)

"""

import numpy as np

# -------------------------------

class Course_Schedule():
    def __init__(self, courses):
        self.courses = courses
        self.schedule = np.zeros((self.courses, 1), dtype="U16")

    def add(self, course):
        self.course = np.array(course)
        np.concatenate((self.schedule, self.course))
        return str(self.schedule)
        
    def __str__(self):
        return str(self.schedule)

# -------------------------------

class Course:
    
    def __init__(self, rubric, number):
        self.rubric = rubric
        self.number = number

    def __str__(self):
        return self.rubric+" "+str(self.number)

# -------------------------------

def main():

    my_courses = Course_Schedule(3)
    course_1 = Course("CSCI", 127)
    my_courses.add(course_1)
    course_2 = Course("M", 171)
    my_courses.add(course_2)
    course_3 = Course("WRIT", 101)
    my_courses.add(course_3)
    print(my_courses)
    
# -------------------------------

main()
