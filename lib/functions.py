#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


greet_programmer()


def greet(name):
    print("Hello, " + name + "!")


greet("John")


def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")


greet_with_default("John")
greet_with_default()


def add(num1, num2):
    return num1 + num2


result = add(2, 8)
print(result)


def halve(number):
    return number/2


result = halve(14)
print(result)
