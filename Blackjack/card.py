from random import choice


class Card():
    def __init__(self) -> None:
        self.shape = choice(["♦", "♥", "♠", "♠"])
        self.value = choice(["A", "2", "3", "4", "5",
                            "6", "7", "8", "9", "10", "K", "Q", "J"])

    def RenderFront(self):
        a = f'''|__{self.value}|''' if self.value != "10" else f'''|_{self.value}|'''
        b = f'''|{self.value}  |''' if self.value != "10" else f'''|{self.value} |'''
        return [f''' ___ ''', b, f'''| {self.shape} |''',
                a]

    def RenderBack(self):
        return [f''' ___ ''', f'''|#  |''', f'''| # |''',
                f'''|__#|''']
