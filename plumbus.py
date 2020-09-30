"""
with open("random_thing.txt", "r") as inFile:
    firstLine = inFile.readline()

    for line in inFile:
        lists = line.split(",")

        p1 = int(lists[1])
        p2 = int(lists[2])

        result = (p1 + p2) / 2
        
        print(result)
"""
reverseHello = []
hello = [[-44, 15, 1], ["hi", 52, "bye"]]

#print(hello[0][2] + hello[1][1])
#print(hello[::-1])


dictionary = {}

dictionary['"'] = "11223344"

print(dictionary.get('"'))
