# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:10:26 2019

@author: Riley
"""

homeruns = {}

homeruns["Babe Ruth"] = 713
homeruns["Mockey Mantle"] = 536
homeruns["John Paxton"] = 0
print(homeruns)

homeruns["Babe Ruth"] = 714
print(homeruns)
homeruns["Babe Ruth"] += 1

del homeruns["John Paxton"]
# If you don't give a key it deletes the whole dictionary

print(homeruns)

csci127students = {"hayden": 17, "devan": 18}

print(csci127students)

csci127students["greg"] = 19

print(csci127students)


import string

# ---------------------------

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_lowercase:
                modified_text += letter

    file.close()
    return modified_text

# ---------------------------

def create_dictionary(text):
    dictionary = {}
    for letter in string.ascii_lowercase:
        dictionary[letter] = 0
    for letter in text:
        dictionary[letter] += 1
    return dictionary

# ---------------------------
    
def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(key, value)

# ---------------------------

text = keep_letters("raven.txt")
letter_count = create_dictionary(text)
print_dictionary(letter_count)
        