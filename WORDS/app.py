import re

def Main():
    word: str = "SNAKE".upper()
    guess: str = input("Guess a 5 letter word\n").upper().strip()
    if not re.match(r"[\w]+", guess):
        return "Error"
    board = CheckGuess(word=word, guess=guess)
    newBoard: list = list(map(lambda x: f"_{x[2].lower()}_" if x[0] == 1 else x[2] if x[0] == 2 else "_", board))
    print(newBoard)
    return "Success"

def CheckGuess(word: str, guess: str):
    res: list = []
    if len(word) != len(guess):
        return res
    for i, g in enumerate(guess):
        check = False
        for j, w in enumerate(word):
            if g == w and i == j:
                res.append([2, g, w])
                check = True
                word = word.replace(g, "_", 1)
                break
            elif g == w and i != j:
                res.append([1, g, w])
                check = True
                break
        if not check:
            res.append([0, g, ""])
    return res
                
             
             

if __name__ == '__main__':
    Main()