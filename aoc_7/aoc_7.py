print("Advent of Code - Day 7")

import collections


def read_input(filename):
    with open(filename) as infile:
        # bag_dict = collections.OrderedDict()
        bag_dict = {}
        for line in infile:
            line = line.strip("\n")
            line = line.strip(".")
            line = line.replace("contain", ",")
            line = line.split(",")

            bag_description = line[0].split()
            bag_description = bag_description[0] + " " + bag_description[1]
            bag_contains = line[1:]

            bag_dict[bag_description] = {}

            for bag in bag_contains:
                bag = bag.split()
                bag_num = bag[0]

                # Probably dont need to care about empty bags
                if bag_num == "no":
                    bag_num = 0
                    bag_dict[bag_description][bag_desc] = bag_num
                #     # continue

                else:
                    bag_num = int(bag_num)
                    bag_desc = bag[1] + " " + bag[2]
                    bag_dict[bag_description][bag_desc] = bag_num

    return bag_dict


def get_sub_bags(bag_colour, bag_dict):
    return bag_dict.get(bag_colour)


def bags_containing_colour(desc, bag_dict):
    sub_colours = get_sub_bags(desc, bag_dict)
    if sub_colours:
        bags_containing_colour(sub_colours[1], bag_info_test)
        # for i in sub_colours:
        #     print(sub_colours, i, get_sub_bags(i, bag_dict))
    else:
        print(sub_colours, get_sub_bags(sub_colours, bag_info_test))


bag_info_test = read_input("aoc_7_input_test.txt")

print(bag_info_test)

# for colour in bag_info_test:
#     bags_containing_colour(colour, bag_info_test)

# for bag in bag_info_test:
#     bags_containing_colour(bag, bag_info_test)
#
#
# bag_info = read_input("aoc_7_input.txt")
