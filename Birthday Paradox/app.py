from pyinputplus import inputNum, inputChoice
from random import randint, choice
import logging
from data import BIRTHDAYS, keys
from collections import Counter

logging.basicConfig(filename="app.log",
                    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)

maxSimulations = 100000


def Main():
    '''
    Title: Birthday Paradox
    Author: Delali Funani
    Inspire by Al Sweigart al@inventwithpython.com
    '''

    simulations = inputNum(
        "How many birthdays shall I generate? (Max 100)\n", min=1, max=100)
    print(f"Here are {simulations} birthdays:")

    birthdays = [f"{key} {BIRTHDAYS(key)}" for key in [choice(keys)
                                                       for i in range(simulations)]]
    temp = list(Counter(birthdays).items())
    temp.sort(reverse=True, key=lambda e: e[1])
    print(temp)
    if temp[0][1] > 1:
        print(
            f"In this simulation, multiple people have a birthday on {temp[0][0]}")
    else:
        print('In this simulation, there are no matching birthdays.')

    print(
        f"Generating {simulations} random birthdays {maxSimulations} times...")
    inputChoice(prompt="Press Enter to begin...", choices=[""], blank=True)
    print(f"Let's run another {maxSimulations} simulations.")
    print("0 simulations run...")

    count = 0
    for index, value in enumerate(range(maxSimulations), 1):
        birthdays = [f"{key} {BIRTHDAYS(key)}" for key in [choice(keys)
                                                           for i in range(simulations)]]

        for index2, value in enumerate(birthdays, 1):
            if value in birthdays[index2:]:
                count += 1
                break

        if index % 10000 == 0:
            print(
                f"{index} simulations run...")

    print(f'''Out of {maxSimulations} simulations of {simulations} people, there was a
matching birthday in that group {count} times. This means
that {simulations} people have a {round((count/maxSimulations) * 100,2)}% chance of
having a matching birthday in their group.
That's probably more than you would think!''')


if __name__ == "__main__":
    Main()
