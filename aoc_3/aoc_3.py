print("Advent of Code - Day 3")


def read_input(data, x_grad, y_grad):
    # The map repeats itself, so need to find out how many times it repeats horizontally to let the sled reach
    # the bottom of the map
    mult = x_grad // y_grad + 1

    tree_map = []

    with open(data, "r") as infile:
        lines = infile.readlines()
        extended_map = mult * (len(lines) // len(lines[0]))
        for line in lines:
            tree_map.append(extended_map * line.strip("\n"))

    return tree_map


def trees_hit(filename, x_grad, y_grad):

    tree_map = read_input(filename, x_grad, y_grad)
    # Max Y value = End of map, 323 rows
    height = len(tree_map)
    # Starting positions 0,0
    x_coord = 0
    y_coord = 0
    # Hit count
    hit_tree_count = 0

    # Convert each string to a list and check x index to see if it is a tree or not
    while y_coord < height:
        s = list(tree_map[y_coord])
        if s[x_coord] == "#":
            hit_tree_count += 1

        # Move x columns across and y rows down
        x_coord += x_grad
        y_coord += y_grad

    return hit_tree_count


def multiply_results(results):
    total = 1
    for x in results:
        total *= x
    return total


def main():

    no_of_trees_hit = []

    no_of_trees_hit.append(trees_hit("advent_day_3_input.txt", x_grad=1, y_grad=1))
    no_of_trees_hit.append(trees_hit("advent_day_3_input.txt", x_grad=3, y_grad=1))
    no_of_trees_hit.append(trees_hit("advent_day_3_input.txt", x_grad=5, y_grad=1))
    no_of_trees_hit.append(trees_hit("advent_day_3_input.txt", x_grad=7, y_grad=1))
    no_of_trees_hit.append(trees_hit("advent_day_3_input.txt", x_grad=1, y_grad=2))

    return multiply_results(no_of_trees_hit)


print(main())
