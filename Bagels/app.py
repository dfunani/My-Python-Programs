import pyinputplus as pyip
import random

'''
    Bagels, a deductive logic game.
        Inspired by: By Al Sweigart al@inventwithpython.com
        User is prompted with: User is prompted to guess a number. If guess is not correct, then user is informed if any of the digits guessed are matched:
                Pico         One digit is correct but in the wrong position.
                Fermi        One digit is correct and in the right position.
                Bagels       No digit is correct.
        User has 10 attempts to guess the 3 digit number or it's Game Over.
'''

Start, End = (100, 999)
Guesses = 10


def main():
    gameState = "yes"

    print('''I am thinking of a 3-digit number. Try to guess what it is.

		Here are some clues:
		When I say:    That means:
		Pico         	One digit is correct but in the wrong position.
		Fermi        	One digit is correct and in the right position.
		Bagels       	No digit is correct.

  ''')
    while gameState[0] == "y":
        randomNum = RandomNumberGenerator(Start, End)

        print(
            f'''I have thought up a number, and You have {Guesses} guess(s) to get it.''')

        for index, value in enumerate(range(Guesses), 1):
            guess = pyip.inputNum((f"Guess #{index}\n"), min=Start, max=End)

            if guess == randomNum:
                print("You got it!")
                break

            print(" ".join(CheckClues(guess, randomNum)))

        print("Number: " + str(randomNum))
        gameState = pyip.inputYesNo("Do you want to play again?\n").lower()


def RandomNumberGenerator(a: int, b: int):
    return random.randint(a, max(a, b))


def CheckClues(userGuess: int, randomNumber: int):
    clues: int = []
    for guessValue, randomValue in zip(str(userGuess), str(randomNumber)):
        if guessValue == randomValue:
            clues.append("Fermi")
        elif guessValue in str(randomNumber):
            clues.append("Pico")

    if not clues:
        clues.append('Bagels')

    clues = sorted(clues)
    return clues


if __name__ == '__main__':
    main()
