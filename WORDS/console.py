from rich import console, theme

WINDOW = console.Console(width=80, theme=theme.Theme({"warning": "red on yellow"}))

def Load_Game(headline: str) -> str:
    WINDOW.clear()
    
    WINDOW.rule(f"[bold blue]:bee: {headline} :bee:[/]\n")
    
    return "Game Started"

def Show_Empty(length: int, rows: int):
    res = (("_" * length) + "\n") * rows
    WINDOW.print(res, justify="center")
    
def Show_Guess(board: list):
    GUESS: str = "" 
    for element in board:
        GUESS += f"[bold white on green]{element[1]}[/]" if element[0] == 2 else f"[bold white on red]{element[1]}[/]" if element[0] == 1 else f"[dim]{element[1]}[/]"
    WINDOW.print(GUESS, justify="center")
    
def Show_Guesses(boards: list, length: int, round: int, alphabet: dict):
    Load_Game(f"GUESS {round}")
    for board in boards:
        Show_Guess(board)
        length = len(board)
    Show_Empty(length, 6 - len(boards))
    Show_Alpha(alphabet)
    
def Show_Alpha(alphabet: dict):
    GUESS: str = "" 
    for element, val in alphabet.items():
        GUESS += f"[bold white on green]{element}[/]" if val == 2 else f"[bold white on red]{element}[/]" if val == 1 else f"[dim]{element}[/]"
    WINDOW.print(GUESS, justify="center")
    
def Show_Error(Error: str):
    WINDOW.print(Error, style="warning")