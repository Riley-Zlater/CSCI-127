# --------------------------------------
# CSCI 127, Lab 7                      |
# October 14, 2019                     |
# Riley Slater                         |
# --------------------------------------

# --------------------------------------
# create_dictionary makes a dictionary of the 
# ascii binary codes as the values and their
# corresponding letter as the keys.
# --------------------------------------

def create_dictionary(file_name):
    dictionary = {}
    with open(file_name, 'r') as file:
        for line in file:
            numbers = line.split(',')
            
            if numbers[1] == "space\n":
                dictionary[" "] = numbers[0]
            elif numbers[1] == "comma\n":
                dictionary[","] = numbers[0]
            else:
                dictionary[numbers[1][:1]] = numbers[0]
            
        file.close()
        return (dictionary)
    
# --------------------------------------
# translate sifts through the dictionary by
# putting each letter of the input sentence
# into the dictionary as the key to find the
# ascii code. Then it appends the sentence
# and the ascii code to a new file.
# --------------------------------------
        
def translate(sentence, dictionary, file_name):
    result = ""
    result_letter = ""
    result_dict = ""
    final = ""
    
    with open(file_name, 'a') as file:
        letters = list(sentence)
    
        for letter in letters:
            result_letter = letter
            result_dict = dictionary.get(letter, "UNKNOWN")
            result = result_letter," ", result_dict + "\n"
            final = ''.join(result)
            file.write(final)
        file.close()
          
# --------------------------------------
# main provides the ascii-codes.csv file
# and prints the dictionary created from that file.
# Then provides the sentences  for translation and
# and gives the file names that will be appended to.
# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")
    print(dictionary)
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

main()
