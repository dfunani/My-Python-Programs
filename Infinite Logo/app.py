import bext
import random
import time
import sys

width, height = bext.size()

try:
    x = int(width/2)
    y = int(height/2)
    bext.goto(x, y)
    print("DVD")
    heading = "unknown"
    mh = 0
    mw = 0
    while True:
        if heading == 'unknown':
            mh = random.choice([-1, 1])
            mw = random.choice([-1, 1])
            heading = 0

        if x < 2:
            mw = 1
        elif x > width - 2:
            mw = -1

        if y < 2:
            mh = 1
        elif y > height - 2:
            mh = -1

        x = max(x - 1, 1) if mw == -1 else min(x + 1, width - 1)
        y = max(y - 1, 1) if mh == -1 else min(y + 1, height - 1)

        if x == width - 1 and y == height - 1:
            # Windows has weird behavior where a character at the end of the row always moves the cursor to the next row.
            continue

        bext.goto(x, y)
        print("DVD")
        time.sleep(0.25)
except KeyboardInterrupt:
    pass
