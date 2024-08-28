#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count = count - 1
    print("Happy New Year!")
    
    pass

def square_integers(int_list):
    return [x**2 for x in int_list]

if __name__ == "__main__":
    positive_integers = [1, 2, 3, 4, 5]
    negative_integers = [-1, -2, -3, -4, -5]
    
    squared_positives = square_integers(positive_integers)
    squared_negatives = square_integers(negative_integers)
    
    print(f"Squared positive integers: {squared_positives}")
    print(f"Squared negative integers: {squared_negatives}")


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()

    pass
