# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# November 5, 2019                                    |
# Riley Slater                                        |
# -----------------------------------------------------

class Queue():
    def __init__(self, numbers):
        self.numbers = []

    def __iadd__(self, other):          
        self.numbers.append(other)
        return self

    def __str__(self):
        return "Contents: " + " ".join(map(str,(self.numbers)))

    def is_empty(self):
        return self.numbers == []

    def enqueue(self, variable):
        self.numbers.append(variable)

    def dequeue(self):
        return self.numbers.pop(0)
    
# -----------------------------------------------------

def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15
    
    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
