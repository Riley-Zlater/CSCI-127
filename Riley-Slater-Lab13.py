import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# November 26, 2019                               |
# Riley Slater                                    |
# -------------------------------------------------

def main(file_name):
    files = pd.read_csv(file_name)

    labels = []
    for titles in files.columns:
        labels.append(titles)
        
    colors = ["blue"]
    for alt in range(len(files)):
        if colors[alt] == "blue":
            colors.append("gold")
        else:
            colors.append("blue")       

    x_axis = labels[0]
    y_axis = labels[1]
    
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"

    files.plot(x=x_axis, y=y_axis, kind="bar", title=file_name[:-4], legend=False, color=colors)

    # The only four statements that may use the matplotlib library appear next.
    # Do not modify them.
    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    

    interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("MSU College Enrollments.csv")
main("CS Faculty.csv")
