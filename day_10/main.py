import os
from art import logo


def addition(n1, n2):
    return n1 + n2

def substraction(n1, n2):
    return n1 - n2

def mulification(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operation = {
    "+": addition,
    "-": substraction,
    "*": mulification,
    "/": division
}


def calculator():
    flag = True
    print(logo)
    n1 = float(input("What's your first number: "))
    print("+\n-\n*\n/\n")
    while flag:
        op = input("Pick the operation: ")
        n2 = float(input("What's your next number: "))
        result = operation[op](n1, n2)
        print(n1, op, n2, "=", result)
        answer = input(f"Type 'yes' to continue calculating with {result}, or type 'no' to start new calculation: ")
        if answer == 'yes':
            n1 = result
        else:
            flag = False
            os.system("cls")
            calculator()

calculator()


