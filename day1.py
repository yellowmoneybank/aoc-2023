from aoc import get_input
import re


def firstDigit(date):
    str = ""
    for i in range(len(date)):
        str = date[i:]

        if  re.search("\d", str[0]):
            return str[0]
        if str.startswith("one"):
            return "1"
        if str.startswith("two"):
            return "2"
        if str.startswith("three"):
            return "3"
        if str.startswith("four"):
            return "4"
        if str.startswith("five"):
            return "5"
        if str.startswith("six"):
            return "6"
        if str.startswith("seven"):
            return "7"
        if str.startswith("eight"):
            return "8"
        if str.startswith("nine"):
            return "9"
        if str.startswith("zero"):
            return "0"


def lastDigit(date):
    date = date[::-1]
    str = ""
    for i in range(len(date)):
        str = date[i:]

        if  re.search("\d", str[0]):
            return str[0]
        if str.startswith("one"[::-1]):
            return "1"
        if str.startswith("two"[::-1]):
            return "2"
        if str.startswith("three"[::-1]):
            return "3"
        if str.startswith("four"[::-1]):
            return "4"
        if str.startswith("five"[::-1]):
            return "5"
        if str.startswith("six"[::-1]):
            return "6"
        if str.startswith("seven"[::-1]):
            return "7"
        if str.startswith("eight"[::-1]):
            return "8"
        if str.startswith("nine"[::-1]):
            return "9"
        if str.startswith("zero"[::-1]):
            return "0"





data = get_input(1).splitlines()
sum = 0
for date in data:
    # firstDigit(date)
    sum += int(firstDigit(date) + lastDigit(date) )
print(sum)
