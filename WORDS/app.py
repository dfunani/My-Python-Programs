import re
import string
import sys
from console import Load_Game, Show_Guesses, Show_Error
import requests

"""
Project: WORDS
app module - My own implementation of wordle
2 functions Main - entry, CheckGuess - Board Manager, Richly - displays using Rich library
"""

def Main(guesses: list, round: int, dictionary: dict, db: list, word: str):
    """
    Game entry Point
    Alphabet Dictionary is create using the string library
    Player is asked to Guess Word
    Guess is Matched to Random generated word
    Player has 6 Guesses
    Game is displayed in terminal
    dictionary vs board/newBoard board is state bound to the round, while the dictionary is bound to the game
    Returns:
        str: game_state
    """
    
    Load_Game("WORDS")
    Show_Guesses(guesses, len(word), round, dictionary)
    while True:
        guess: str = input(f"Guess a {len(word)} letter word\n").upper().strip()
        if guess.isalpha() and len(word) == len(guess) and guess not in db:
            db.append(guess)
            break
        if not guess.isalpha():
            Show_Error("Only alphabetic characters permitted")
            continue
        if len(word) != len(guess):
            Show_Error(f"Your Guess must be {len(word)} long")
            continue
        if guess in db:
            Show_Error(f"You have already guessed {guess}")
            continue
            
    board = CheckGuess(word=word, guess=guess, dictionary=dictionary)
    guesses.append(board)
    Show_Guesses(guesses, len(word), round, dictionary)
    if guess == word:
        return "Success"
    return "Retry"

def CheckGuess(word: str, guess: str, dictionary: dict) -> str:
    """
    Compares the Guess to the Word generated
    If letter matched in value and 
    Args:
        word (str): Word generated
        guess (str): Players Guess
        dictionary (_type_): Dictionary of letters to maintain letters selected by the guessing user

    Returns:
        dict: maintains the alphabetic letters affected by the guesses
    """
    res: list = []
    for i, g in enumerate(guess):
        check = False
        for j, w in enumerate(word):
            if g == w and i == j:
                res.append([2, g, w])
                check = True
                word = word.replace(g, "_", 1)
                dictionary[g] = 2
                break
            elif g == w and i != j:
                res.append([1, g, w])
                check = True
                word = word.replace(g, "_", 1)
                dictionary[g] = 1 if dictionary[g] and dictionary[g] != 2 else dictionary[g]
                break
        if not check:
            res.append([0, g, ""])
    return res
                

if __name__ == '__main__':
    guesses: list = []
    dictionary: dict = {letter: 0 for letter in string.ascii_uppercase}
    guess_db = []
    word = requests.get("https://random-word-api.herokuapp.com/word").json()
    for i in range(6):
        if Main(guesses, i + 1, dictionary, guess_db, word[0].upper()) == "Success":
            Show_Error(f"You WIN, {word[0]} is the correct GUESS")
            sys.exit()
    Show_Error(f"You LOSE, correct word was {word[0]}")
        