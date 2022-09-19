from random import randint
keys = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]


def BIRTHDAYS(key):
    birthdays = {
        "Jan": randint(1, 31),
        "Feb": randint(1, 28),
        "Mar": randint(1, 31),
        "Apr": randint(1, 30),
        "May": randint(1, 31),
        "Jun": randint(1, 30),
        "Jul": randint(1, 31),
        "Aug": randint(1, 31),
        "Sep": randint(1, 30),
        "Oct": randint(1, 31),
        "Nov": randint(1, 30),
        "Dec": randint(1, 31)
    }
    return birthdays[key]
