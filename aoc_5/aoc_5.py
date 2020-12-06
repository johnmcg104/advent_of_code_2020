print("Advent of Code - Day 5")


def read_input(filename):
    with open(filename, "r") as infile:
        data = [line.rstrip("\n") for line in infile]

    return data


def find_row(seat_identifier):
    # Iterate through seat identifier and chop possible rows range in half depending on the character we see
    rows = list(range(128))
    for char in seat_identifier:
        halfway_rows = len(rows) // 2
        if char == "F":
            rows = rows[:halfway_rows]
        if char == "B":
            rows = rows[halfway_rows:]

    return rows[0]


def find_seat(seat_identifier):
    # Iterate through seat identifier and chop possible columns ranges in half depending on the character we see
    columns = list(range(8))
    for char in seat_identifier:
        halfway_columns = len(columns) // 2
        if char == "L":
            columns = columns[:halfway_columns]
        if char == "R":
            columns = columns[halfway_columns:]

    return columns[0]


def get_seat_id(row_num, seat_num):
    seat_id = row_num * 8 + seat_num

    return seat_id


def get_all_seat_ids(possible_seats):
    all_seat_ids = set()
    for seat in possible_seats:
        row_num = find_row(seat)
        seat_num = find_seat(seat)
        all_seat_ids.add(get_seat_id(row_num, seat_num))

    all_seat_ids = sorted(all_seat_ids)

    return all_seat_ids


def max_seat_id(possible_seats):
    max_id = max(get_all_seat_ids(possible_seats))

    return max_id


def find_empty_seats(possible_seats):
    """
    This doesnt really work, it assumes that all but one row will have all 8 seats taken. The input data set does not
    contain info for all 128 rows, it starts at row 7 seat 7 and ends at row 116 seat 7.
    Will return all row & seat combos that are missing

    :param possible_seats: List of seat identifier info e.g. ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    :return: List of tuples (row, seat, seat id) of empty seats
    """

    # Make a dictionary, each key is row and set equal to a list of taken seats in that row
    row_seats_dict = {}
    for seat in possible_seats:
        seat_row = find_row(seat)
        seat_column = find_seat(seat)
        if row_seats_dict.get(seat_row):
            row_seats_dict[seat_row].append(seat_column)
        else:
            row_seats_dict[seat_row] = [seat_column]

    # # Can check first & last entries and remove if not all 8 seats are in the list of assigned seats
    # if len(row_status[min(row_status)]) != 8:
    #     del row_status[min(row_status)]
    # if len(row_status[max(row_status)]) != 8:
    #     del row_status[max(row_status)]

    missing_seats_list = []
    for row in row_seats_dict:
        row_seats_dict[row] = sorted(row_seats_dict[row])
        taken_seats = row_seats_dict[row]
        if len(taken_seats) != 8:
            missing_row = row
            missing_seats = [x for x in range(8) if x not in taken_seats]
            for seat in missing_seats:
                missing_seat_id = get_seat_id(missing_row, seat)
                missing_seats_list.append((missing_row, seat, missing_seat_id))

    return missing_seats_list


def find_missing_id(possible_seats):
    seat_ids = list(get_all_seat_ids(possible_seats))
    missing_seat_id = [
        x for x in range(seat_ids[0], seat_ids[-1] + 1) if x not in seat_ids
    ]

    return missing_seat_id


print(max_seat_id(read_input("aoc_5_input.txt")))
print(find_empty_seats(read_input("aoc_5_input.txt")))
print(find_missing_id(read_input("aoc_5_input.txt")))
