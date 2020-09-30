# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:19:20 2019

@author: Riley
"""

grocery = {}
grocery["bananas"] = .99
grocery["milk"] = 4.79
grocery["gum"] = .99
grocery["cheese"] = 1.79

print(grocery,"\n")

print(grocery.keys())
print(grocery.values())
print(grocery.items(), "\n")

for key in grocery.keys():
    print(key)
    
print() 
for value in grocery.values():
    print(value)
    
print()   
    
for key, value in grocery.items():
    print(key, value)

print()

for key in grocery.keys():
    grocery[key] += .10
    
for key, value in grocery.items():
    print(key, value)

print()

print(grocery.get("bananas"))
print(grocery.get("cheese"))
print(grocery.get("bread", "Item is not for sale"))


def create_dictionary():
    dictionary = {}
    dictionary["sir"] = "matey"
    dictionary["professor"] = "foul blaggert"
    dictionary["hello"] = "avast"
    return dictionary

# ----------------------------

def translate(dictionary, sentence):
    result = ""
    words = sentence.split()
    for word in words:
        if word in dictionary.keys():
            result += dictionary[word] + " "
        else:
            result += word + " "
    
    return result

# ----------------------------
    
def main():
    piratese = create_dictionary()
    sentence = input("Enter sentence to translate: ")
    sentence = sentence.lower()
    translated_sentence = (translate(piratese, sentence))
    print(translated_sentence)

main()
