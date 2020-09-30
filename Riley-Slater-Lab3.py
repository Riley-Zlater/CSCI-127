# --------------------------------------
# CSCI 127, Lab 3                      |
# September 17, 2019                   |
# Riley Slater                         |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------
import string

def count_built_in(sentence):
    a = sentence.count("a")
    e = sentence.count("e")
    i = sentence.count("i")
    o = sentence.count("o")
    u = sentence.count("u")
    return(a + e + i + o + u)
           
def count_iterative(sentence):
    vowel_counter = 0
    for vowels in sentence:
        if vowels == "a":
            vowel_counter += 1
        elif vowels == "e":
            vowel_counter += 1
        elif vowels == "i":
            vowel_counter += 1
        elif vowels == "o":
            vowel_counter += 1
        elif vowels == "u":
            vowel_counter += 1       
    return(vowel_counter)
        

def count_recursive(sentence):
    if not sentence:
        return 0
    return (1 if sentence[0] in "aeiou" else 0) + count_recursive(sentence[1:])

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
