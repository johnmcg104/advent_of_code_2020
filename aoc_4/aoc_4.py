print("Advent Of Code - Day4")


def read_input(file):
    passports_dict = {}

    with open(file, "r") as infile:
        # No names for passports, will name each entry based on its location in the input file
        passport_entry_number = 1
        separator = "\n"
        for line in infile:
            # If not blank line this must have passport info. Split line to have each field:value as an element in list
            if line != separator:
                line = line.split()
                temp_line = []
                temp_line.extend(line)

                if passport_entry_number not in passports_dict:
                    passports_dict[passport_entry_number] = {}

                for item in temp_line:
                    # Making a dictionary for each passport
                    # E.g 1: {"eyr": 2025, "byr": 1992 ...}
                    entry = item.split(":")
                    key = entry[0]
                    value = entry[1]
                    passports_dict[passport_entry_number][key] = value

            # New entry, stop adding to previous entry. Increase count so next loop will create a new dict key to use
            elif line == separator:
                passport_entry_number += 1

            # else:
            #     raise Exception(f"Invalid line: {line}")

    return passports_dict


def check_value(field, value):
    passed = False

    # ------------------------------------------------------------------------------------------------------------ #
    # Birth Year
    if field == "byr":
        if value.isdigit() and (1920 <= int(value) <= 2002):
            passed = True
    # ------------------------------------------------------------------------------------------------------------ #
    # Issue Year
    if field == "iyr":
        if value.isdigit() and (2010 <= int(value) <= 2020):
            passed = True
    # ------------------------------------------------------------------------------------------------------------ #
    # Expiration Year
    if field == "eyr":
        if value.isdigit() and (2020 <= int(value) <= 2030):
            passed = True
    # ------------------------------------------------------------------------------------------------------------ #
    # Height
    if field == "hgt":
        if (
            value.endswith("cm")
            and value[:-2].isdigit()
            and (150 <= int(value[:-2]) <= 193)
        ):
            passed = True
        if (
            value.endswith("in")
            and value[:-2].isdigit()
            and (59 <= int(value[:-2]) <= 76)
        ):
            passed = True
    # ------------------------------------------------------------------------------------------------------------ #
    # Hair Color
    if field == "hcl":
        if value.startswith("#") and len(value) == 7:
            color = value[-6:].lower()
            allowed_chars = ["a", "b", "c", "d", "e", "f"]
            if all(char in allowed_chars for char in color if char.isalpha()):
                passed = True
    # ------------------------------------------------------------------------------------------------------------ #
    # Eye Color
    if field == "ecl":
        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            passed = True
    # ------------------------------------------------------------------------------------------------------------ #
    # Passport ID
    if field == "pid":
        if len(value) == 9 and value.isdigit():
            passed = True

    return passed


def is_valid(passport_dict):
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]

    first_check = 0
    second_check = 0

    for passport in passport_dict:
        # First check - make sure that the passport entry has all 7 required fields
        if all(passport_dict[passport].get(field) for field in required_fields):
            first_check += 1
            # Second check - confirm if the field values meet the criteria
            second_check_passed = True
            for field in required_fields:
                value = passport_dict[passport][field]
                # Break out of loop as soon as one check fails and move on to next passport
                if check_value(field, value) is False:
                    second_check_passed = False
                    break

            if second_check_passed:
                second_check += 1

    results = f"Passed first check: {first_check}\n" \
              f"Passed second check: {second_check}"

    return results


passports_data = read_input("aoc_4_input.txt")

print(is_valid(passports_data))
