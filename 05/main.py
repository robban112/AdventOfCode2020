import numpy

input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(line.strip())

def is_in_list(element, _list):
    is_in_list = False
    for _list_el in _list:
        if element == _list_el:
            is_in_list = True
    return is_in_list

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def board_pass_id(board_pass):
    num_rows = 128
    min_row = 0
    max_row = 127
    for char in board_pass[:-3]:
        num_rows = num_rows / 2
        if char == 'F':
            max_row = max_row - num_rows
        if char == 'B':
            min_row = min_row + num_rows
    num_columns = 8
    min_column = 0
    max_column = 7
    for char in board_pass[-3:]:
        num_columns = num_columns / 2
        if char == 'L':
            max_column = max_column - num_columns
        if char == 'R':
            min_column = min_column + num_columns
    return (max_row, max_column)


def part_one(mylist):
    max_seat = 0
    for line in mylist:
        (max_row, max_column) = board_pass_id(line)
        seat = (max_row * 8) + max_column
        if seat > max_seat:
            max_seat = seat
    print(max_seat)

def part_two(mylist):
    board_passes = []
    ids = []
    for line in mylist:
        (row, col) = board_pass_id(line)
        seat_id = (row * 8) + col
        board_passes.append((row, col, seat_id))
        ids.append(seat_id)
    for (row, col, _id) in board_passes:
        for (row_2, col_2, _id_2) in board_passes:
            if _id == _id_2 - 2:
                if row != 0 and row != 127:
                    if not is_in_list(_id + 1, ids):
                        print(_id + 1)

def main():
    part_two(input_list)

main()