print("Advent of Code - Day 6")


def read_input(filename):
    with open(filename) as infile:
        separator = "\n"
        answers_dict = {}
        group_num = 1
        for line in infile:
            if line != separator:
                if group_num not in answers_dict:
                    answers_dict[group_num] = set()

                answers_dict[group_num].add(line.strip("\n"))

            if line == separator:
                group_num += 1

        return answers_dict


def combine_group_answers(group_answers):
    combined_answers_dict = {}
    for group in group_answers:
        temp_set = list("".join(group_answers[group]))
        combined_answers_dict[group] = temp_set

    return combined_answers_dict


def get_unique_answers(group_answers):
    unique_answers_dict = {}
    for group in group_answers:
        temp_set = set(group_answers[group])
        unique_answers_dict[group] = temp_set

    return unique_answers_dict


def get_sum_unique(all_answers):
    total = 0
    for answer_set in all_answers:
        total += len(all_answers[answer_set])

    return total


def everyone_yes(group_answers):
    for group in group_answers:
        no_of_people = len(group_answers[group])
        for char in set(group_answers[group]):
            print()


group_answers_1 = read_input("aoc_6_input.txt")
combined_answers_1 = combine_group_answers(group_answers_1)
unique_answers_1 = get_unique_answers(combined_answers_1)
sum_unique_answers = get_sum_unique(unique_answers_1)

# print(sum_unique_answers)

print(everyone_yes(group_answers_1))