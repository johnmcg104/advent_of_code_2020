print("Advent of code - day 2")


def read_input(filename):
    data = []
    with open(filename, "r") as infile:
        for line in infile:
            new_line = line.split()
            if len(new_line) == 3:
                appearances = new_line[0].split("-")
                min_appearances = int(appearances[0])
                max_appearances = int(appearances[1])
                special_char = new_line[1][0]
                password = new_line[2]
                data.append([min_appearances, max_appearances, special_char, password])
    return data


def first_check(input):
    valid_passwords_1 = 0
    invalid_passwords_1 = 0
    for entry in input:
        min_appearances = int(entry[0])
        max_appearances = int(entry[1])
        special_char = entry[2]
        password = entry[3]
        if min_appearances <= password.count(special_char) <= max_appearances:
            valid_passwords_1 += 1
        else:
            invalid_passwords_1 += 1

    results = f"""
    First check:
    Valid: {str(valid_passwords_1)}
    Invalid: {str(invalid_passwords_1)}
    """
    return results


def second_check(input):
    valid_passwords_2 = 0
    invalid_passwords_2 = 0
    for entry in input:
        first_location = int(entry[0])
        second_location = int(entry[1])
        special_char = entry[2]
        password = entry[3]
        min_check = password[first_location - 1] == special_char
        max_check = password[second_location - 1] == special_char
        if min_check + max_check == 1:
            valid_passwords_2 += 1
        else:
            invalid_passwords_2 += 1
    results = f"""
    Second check:
    Valid: {str(valid_passwords_2)}
    Invalid: {str(invalid_passwords_2)}
    """

    return results


input_data = read_input("advent_of_code_2_input.txt")
print(first_check(input_data))
print(second_check(input_data))
