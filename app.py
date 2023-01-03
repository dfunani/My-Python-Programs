import sys
from pyinputplus import inputNum

def Main():
    num = None
    if len(sys.argv) > 1:
        num = sys.argv[1]
    else:
        num = inputNum(prompt="Enter a starting number (greater than 0) or (0) to QUIT:", min=0)
    result = []
    while num != 1:
        result.append(int(num))
        if num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1
    result.append(1)
    print(*result, sep=", ")

if __name__ == '__main__':
    Main()