import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive


def display1(file_name):
    file = pd.read_csv(file_name)
    
    consoles = []
    all_consoles = []
    
    for loop in file["Release.Console"]:
        all_consoles.append(loop)
        if loop not in consoles:
            consoles.append(loop)

    DS = 0
    PSP = 0
    X360 = 0
    Wii = 0
    PS3 = 0

    for loop in all_consoles:
        if loop == consoles[0]:
            DS+=1
        elif loop == consoles[1]:
            PSP+=1
        elif loop == consoles[2]:
            X360+=1
        elif loop == consoles[3]:
            Wii+=1
        else:
            PS3+=1
            
    total_consoles = [DS, PSP, X360, Wii, PS3]

    DataSet = list(zip(consoles, total_consoles))
    data = pd.DataFrame(data = DataSet, columns=["Consoles", "Games"])

    data.plot(x="Consoles",y="Games", kind="bar", color=["blue", "black", "green", "purple", "grey"], legend=False)
    plt.title("Total Games For Each Console")
    plt.ylabel("# of Games")
    plt.xlabel("Consoles Avaliable")

def display2(file_name):
    file = pd.read_csv(file_name)
    handheld_counter = 0
    total_counter = 0
    for loop in file["Features.Handheld?"]:
        total_counter+=1
        if loop == True:
            handheld_counter+=1
    
    x = ["Handheld", "Not Handheld"]
    y = [handheld_counter, (total_counter-handheld_counter)]
    
    data = pd.DataFrame(data = y, index=x)

    data.plot(y=0, kind="pie", legend=True)
    plt.title("Handheld Games Vs Not Handheld Games")


def main(file):
    display1(file)
    display2(file)
    interactive(True)
    plt.show()

main("video_games.csv")
