import collections
import time

input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(line)


def get_min_max_ocurr(list_line):
    _split = list_line.split(" ")
    (min_ocurr, max_ocurr) = _split[0].split("-")
    return (int(min_ocurr), int(max_ocurr))

def get_letter(list_line):
    return list_line.split(" ")[1][0]

def get_password(list_line):
    return list_line.split(" ")[2]

def validate_line(list_line):
    (min_ocurr, max_ocurr) = get_min_max_ocurr(list_line)
    letter = get_letter(list_line)
    password = get_password(list_line)
    occurr = 0
    for c in password:
        if c == letter:
            print("occurred")
            occurr += 1
    print(occurr, min_ocurr, max_ocurr, letter)
    if occurr >= min_ocurr and occurr <= max_ocurr:
        return True
    else: 
        return False

def validate_line_second(list_line):
    (position_one, position_two) = get_min_max_ocurr(list_line)
    letter = get_letter(list_line)
    password = get_password(list_line)
    correct_positions = 0
    if position_one - 1 >= 0:
        if password[position_one - 1] == letter:
            correct_positions += 1
    if position_two - 1 >= 0:
        if password[position_two - 1] == letter:
            correct_positions += 1
    
    if correct_positions == 1:
        return True
    else:
        return False

    # if (pos_1 and pos_2) or (not pos_1 and not pos_2):
    #     print(position_one, position_two, letter, password, pos_1, pos_2, 'False')
    #     return False
    # else:
    #     print(position_one, position_two, letter, password, pos_1, pos_2, 'True')
    #     return True


def first_part(mylist):
    valid_passwords = 0
    for line in mylist:
        if validate_line(line):
            valid_passwords += 1
    print(valid_passwords)

def second_part(mylist):
    valid_passwords = 0
    for line in mylist:
        if validate_line_second(line):
            valid_passwords += 1
    print(valid_passwords)

def main():
    second_part(input_list)

    # savedFrequencies = []
    # freq = 0
    # while True:
    #     for ch in changes:
    #         freq += ch
    #         if freq in savedFrequencies:
    #             print(freq)
    #             return
    #         savedFrequencies.append(freq)


main()