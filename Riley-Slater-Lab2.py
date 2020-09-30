# --------------------------------------+
# CSCI 127, Joy and Beauty of Data      |
# Lab 2: Tax Calculator                 |
# Riley Slater                          |
# Date: September 09, 2019              |
# --------------------------------------+
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2018.  |
# --------------------------------------+


def unmarried_individual_tax(income): #This function compounds each tax bracket
    if income <= 9700:
        return(income * .1)
    elif 9700 <= income < 39475:
        return((9700*.1)+(income-9700)*.12)
    elif 39475 <= income < 84200:
        return((9700*.1)+(29775*.12)+(income-39475)*.22)
    elif 84200 <= income < 160725:
        return((9700*.1)+(29775*.12)+(44725*.22)+(income-84200)*.24)
    elif 160725 <= income < 204100:
        return((9700*.1)+(29775*.12)+(44725*.22)+(76525*.24)+(income-160725)*.32)
    elif 204100 <= income < 510300:
        return((9700*.1)+(29775*.12)+(44725*.22)+(76525*.24)+(43375*.32)+(income-204100)*.35)
    else:
        return((9700*.1)+(29775*.12)+(44725*.22)+(76525*.24)+(43375*.32)+(306200*.35)+(income-510300)*.37)
    
# ---------------------------------------

def process(income):
    print("The 2018 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():
    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7

# ---------------------------------------

main()
