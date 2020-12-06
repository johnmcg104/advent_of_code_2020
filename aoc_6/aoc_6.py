print("Advent of Code - Day 6")


def read_input(filename):
    with open(filename) as infile:
        separator = "\n"
        answers_dict = {}
        group_num = 1
        for line in infile:
            if line != separator:
                if group_num not in answers_dict:
                    answers_dict[group_num] = []

                answers_dict[group_num].append(line.strip("\n"))

            if line == separator:
                group_num += 1

        return answers_dict


def combine_group_answers(group, group_answers):
    combined_answers = list("".join(group_answers[group]))

    return combined_answers


def get_unique_answers(answers):
    unique_answers = list(set(answers))

    return unique_answers


def get_sum_unique(all_answers):
    total = 0
    for answer_set in all_answers:
        total_answers = combine_group_answers(answer_set, all_answers)
        unique_answers = get_unique_answers(total_answers)
        total += len(unique_answers)

    return total


def everyone_yes(group_answers):
    result = 0
    for group in group_answers:
        groups_size = len(group_answers[group])
        combined_answers = combine_group_answers(group, group_answers)
        unique_answers = get_unique_answers(combined_answers)

        for answer in unique_answers:
            if groups_size == combined_answers.count(answer):
                result += 1

    return result


group_answers_1 = read_input("aoc_6_input.txt")

sum_unique_answers = get_sum_unique(group_answers_1)
everyone_yes_count = everyone_yes(group_answers_1)

print(sum_unique_answers)
print(everyone_yes_count)
