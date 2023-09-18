# Create a simple Python program that asks the user for their name and greets them
"""
name = input("What is your name?")
age = input("How old are you?")
print("Nice to meet you," + name + "!" + " You're" + age + " years old!")
"""

# Write a program that calculates and prints the Fibonacci sequence up to a given number.
def fib(n):
    if n < 1 :
        return
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    fib(5)