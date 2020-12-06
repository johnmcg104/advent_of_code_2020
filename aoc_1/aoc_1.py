from itertools import combinations

print("Advent of Code - Day 1")


def read_input(filename):
    with open(filename) as infile:
        input_data = [
            int(line.strip("\n")) for line in infile if line.strip("\n").isdigit()
        ]

    return input_data


def get_combination(data, values):
    combos = list(combinations(data, values))
    for combo in combos:
        total = sum(list(combo))
        if total == 2020:
            return combo


def get_multiplied_values(combo):
    res = 1
    for value in combo:
        res *= value
    return res


aoc_1_data = read_input("aoc_1_input.txt")
two_values = get_combination(aoc_1_data, 2)
two_mult = get_multiplied_values(two_values)
three_values = get_combination(aoc_1_data, 3)
three_mult = get_multiplied_values(three_values)

print(two_values, two_mult)
print(three_values, three_mult)
