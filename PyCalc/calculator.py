from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
from functools import partial


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.inputBox = InputBox()
        self.layout.addWidget(self.inputBox)
        self.keypad = KeyPad(self.inputBox)
        self.layout.addLayout(self.keypad)


class InputBox(QLineEdit):
    _DISPLAY_HEIGHT = 35 * 2

    def __init__(self) -> None:
        super().__init__()
        self.setFixedHeight(self.DISPLAY_HEIGHT)
        self.setReadOnly(True)
        self.setStyleSheet(
            "border: 2px solid black; border-radius: 5; font-size: 20px; background-color: white")

    @property
    def DISPLAY_HEIGHT(self):
        return self._DISPLAY_HEIGHT


class KeyPad(QGridLayout):
    KEYBOARD = [
        ["7", "8", "9", "/", "C"],
        ["4", "5", "6", "*", "("],
        ["1", "2", "3", "-", ")"],
        ["0", "00", ".", "+", "="],
    ]

    BUTTONS = {}

    BUTTON_HEIGHT = 40 * 2

    def __init__(self, inputBox) -> None:
        super().__init__()
        self._create_buttons(inputBox)

    def _create_buttons(self, inputBox):
        for i, row in enumerate(self.KEYBOARD):
            for j, key in enumerate(row):
                self.button = QPushButton(key)
                self.button.setStyleSheet(
                    "border: 2px solid black; border-radius: 5; font-size: 20px; background-color: white")
                self.button.setFixedSize(
                    self.BUTTON_HEIGHT, self.BUTTON_HEIGHT)
                self.button.clicked.connect(
                    partial(self.click_handler, key, inputBox))
                self.BUTTONS[key] = self.button
                self.addWidget(self.button, i, j)

    def click_handler(self, key, box):
        if key == "C":
            box.setText(box.text()[0:-1])
        elif key == "=":
            try:
                res = eval(box.text())
                box.setText(str(res))
            except Exception:
                box.setText("")
            self.EVALUATED = True
        else:
            box.setText(box.text() + key)
