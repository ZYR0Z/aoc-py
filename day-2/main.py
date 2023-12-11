import re


def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r"(\d+) (\w+)", line)
    return max(int(count) for count, color in cubes if color == comparison_color)


with open("./day-2/input.txt") as f:
    lines = f.readlines()
    games = []

    for line in lines:
        games.append(
            max_cubes(line, "red") * max_cubes(line, "green") * max_cubes(line, "blue")
        )

print(sum(games))
