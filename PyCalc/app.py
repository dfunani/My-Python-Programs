"""pycalc.app
PyQT built calculator
"""
from window import *
import sys


def main():
    app = App()
    window = Window("PyCalc")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
