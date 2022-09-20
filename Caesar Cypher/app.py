import pyinputplus as py


def Main():
    typeCrypt = py.inputChoice(prompt="Do you want to (e)ncrypt or (d)ecrypt?\n>",
                               choices=["e", "d"])
    typeCrypt = typeCrypt.lower()
    key = py.inputNum(
        prompt="Please enter the key (0 to 25) to use.\n>", min=0, max=25)

    message = input("Enter the message to encrypt.\n >")

    if typeCrypt.lower() == 'd':
        print(decrypt(message, key))
    elif typeCrypt.lower() == 'e':
        print(encrypt(message, key))
    else:
        sys.exit("something went wrong")


def encrypt(msg, key):
    result = ""
    for char in msg:
        temp = ord(char) + key
        if (ord(char) > 64 and ord(char) < 91) and temp > 90:
            temp = 64 + (temp - 90)
        elif (ord(char) > 96 and ord(char) < 123) and temp > 122:
            temp = 96 + (temp - 122)
        elif (ord(char) > 47 and ord(char) < 58) and temp > 57:
            temp = 47 + (temp - 57)
        elif (ord(char) > 31 and ord(char) < 48) and temp > 47:
            temp = 31 + (temp - 47)
        elif (ord(char) > 57 and ord(char) < 65) and temp > 64:
            temp = 57 + (temp - 64)
        elif (ord(char) > 90 and ord(char) < 97) and temp > 96:
            temp = 90 + (temp - 96)
        elif (ord(char) > 122 and ord(char) < 127) and temp > 126:
            temp = 122 + (temp - 126)

        result += chr(temp)
    return result


def decrypt(msg, key):
    result = ""
    for char in msg:
        temp = ord(char) - key
        if (ord(char) > 64 and ord(char) < 91) and temp < 65:
            temp = 91 + (temp - 65)
        elif (ord(char) > 96 and ord(char) < 123) and temp < 96:
            temp = 123 + (temp - 97)
        elif (ord(char) > 47 and ord(char) < 58) and temp < 48:
            temp = 58 + (temp - 48)
        elif (ord(char) > 31 and ord(char) < 48) and temp < 32:
            temp = 48 + (temp - 32)
        elif (ord(char) > 57 and ord(char) < 65) and temp < 58:
            temp = 65 + (temp - 58)
        elif (ord(char) > 90 and ord(char) < 97) and temp < 91:
            temp = 97 + (temp - 91)
        elif (ord(char) > 122 and ord(char) < 127) and temp < 123:
            temp = 127 + (temp - 123)

        result += chr(temp)
    return result


if __name__ == '__main__':
    Main()
