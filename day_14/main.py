import random
import os

from art import logo, vs
from data import data

def compare():
    array = []
    d = random.choice(data)
    if data.index(d) not in array:
        return d
    array.append(data.index(d))
    return compare()


def play():
    compare_a = compare()
    compare_b = compare()
    score = 0

    print(logo)
    while True:
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
        print(vs)
        print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if (answer == "a" and compare_a["follower_count"] > compare_b["follower_count"]) or\
             (answer == "b" and compare_a["follower_count"] < compare_b["follower_count"]):
            score += 1
            compare_a = compare_b
            compare_b = compare()
            print(f"Your current socre is {score}")

        else:
            os.system("cls")
            print(logo)
            print(f"Sorry that's wrong. Final score: {score}")
            break

if "__main__" == __name__:
    play()

