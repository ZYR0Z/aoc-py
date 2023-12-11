import re

numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def convert(value):
    if value is not None:
        if value.isdigit():
            return int(value)
        if value in numbers:
            return int(numbers.index(value))


with open("./day-1/input.txt") as f:
    lines = f.readlines()

    count = 0

    for line in lines:
        dictionary = {}

        # Get digit indexes
        for i, char in enumerate(line):
            if char.isdigit():
                dictionary[i] = convert(char)

        # Using Regex, because i am too stupid to do it in pure python (https://regexlicensing.org/)
        for number in numbers:
            matches = re.finditer(number, line)

            for match in matches:
                dictionary[match.span()[0]] = convert(number)

        # Only get the first an last number out of the dic
        keys = sorted(dictionary.keys())
        count += (dictionary[keys[0]] * 10) + dictionary[keys[-1]]

    print(count)
