from PyQt6.QtWidgets import QWidget, QDialog, QMainWindow, QToolBar, QStatusBar, QApplication
from calculator import Calculator


class App(QApplication):
    def __init__(self) -> None:
        super().__init__([])


class Window(QMainWindow):
    _WINDOW_SIZE = 235 * 2
    theme = {"True": "Light", "False": "Dark"}
    style = {"Dark": "#E5CFFB", "Light": "#9D7BB0"}
    check = True

    def __init__(self, title) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(self._WINDOW_SIZE, self._WINDOW_SIZE)
        self.menu = self.menuBar().addMenu("Settings")
        self.action = self.menu.addAction(
            self.theme[str(self.check)], self.set_menu)
        self.calculator = Calculator()
        self.setCentralWidget(self.calculator)
        self.setStyleSheet(
            f"background-color: {self.style[self.theme[str(self.check)]]}")

    @property
    def WINDOW_SIZE(self):
        return self._WINDOW_SIZE

    def set_menu(self):
        self.menu.removeAction(self.action)
        """ self.check = False if self.check else True """
        self.check ^= True
        self.action = self.menu.addAction(
            self.theme[str(self.check)], self.set_menu)
        self.setStyleSheet(
            f"background-color: {self.style[self.theme[str(self.check)]]}")

    def create_statusbar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


class Modal(QDialog):
    def __init__(self, title) -> None:
        super().__init__()
        self.setWindowTitle(title)


class App(QApplication):
    def __init__(self) -> None:
        super().__init__([])
