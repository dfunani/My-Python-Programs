def Main():
    with open('bitmapworld.txt', "r") as bitmap:
        phrase = "hello"
        bitlines = bitmap.readlines()
        result = ''
        for i, bitline in enumerate(bitlines):
            for j, bit in enumerate(bitline):
                if bit == " ":
                    print(" ", end="")
                    result += " "
                else:
                    print(phrase[j % len(phrase)], end="")
                    result += phrase[j % len(phrase)]
            print()
            result += "\n"
            with open('output.txt', "w") as file:
                file.write(result)


if __name__ == '__main__':
    Main()
