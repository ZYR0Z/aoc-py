import re  # (https://regexlicensing.org/)


def substring(x: int, y1: int, y2: int) -> str:  # y1 is inclusive, y2 is exclusive
    return (
        data[x][max(y1, 0) : min(y2, len(data[0]))] if x >= 0 and x < len(data) else ""
    )


data = (
    open("./day-3/input.txt").read().splitlines()
)  # no while because we need it also in substring()

part_numbers = []

for x, line in enumerate(data):
    for number in re.finditer(r"\d+", line):
        left = number.start() - 1
        right = number.end()
        adjacent_characters = (
            substring(x - 1, left, right + 1)
            + substring(x, left, left + 1)
            + substring(x, right, right + 1)
            + substring(x + 1, left, right + 1)
        )
        is_part_number = set(adjacent_characters) != {"."}

        if is_part_number:
            part_number = int(number.group())
            part_numbers.append(part_number)

print(sum(part_numbers))
