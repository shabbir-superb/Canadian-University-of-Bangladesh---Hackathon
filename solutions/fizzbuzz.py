"""
FizzBuzz Solution
Prints numbers from 1 to 100 with the following rules:
- For multiples of 3, prints "Fizz"
- For multiples of 5, prints "Buzz"
- For multiples of both 3 and 5, prints "FizzBuzz"
- Otherwise, prints the number
"""

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()
