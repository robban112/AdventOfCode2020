import numpy

def read_input():
    input_list = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            input_list.append(int(line.strip()))
    return input_list

def is_in_list(element, _list):
    is_in_list = False
    for _list_el in _list:
        if element == _list_el:
            is_in_list = True
    return is_in_list

def part_one(mylist):
    one_jolts = []
    three_jolts = []
    mylist.append(mylist[-1] + 3)
    mylist.insert(0, 0)
    for idx, el in enumerate(mylist):
        if idx + 1 < len(mylist):
            next_el = mylist[idx + 1]
            diff = next_el - el
            if diff == 1:
                one_jolts.append(el)
            elif diff == 3:
                three_jolts.append(el)
    print(one_jolts, len(one_jolts))
    print(three_jolts, len(three_jolts))
    print("Result: " + str(len(one_jolts) * len(three_jolts)))

def recursive_count(n):
    if n > 4:
        return recursive_count(n - 1) * 2 - 1
    else:
        return 4

def count_arrangements(one_occurrences):
    count_agg = 1
    for ones in one_occurrences:
        n = len(ones)
        if n > 4:
            count_agg *= recursive_count(n)
        elif n == 4:
            count_agg *= 4
        elif n == 3:
            count_agg *= 2
    return count_agg

def safe_get(index, map):
    if not index in map:
        return 0
    else:
        return map[index]

def part_two(mylist):
    one_occurrences = []
    one_occurr_agg = []
    mylist.append(mylist[-1] + 3)
    mylist.insert(0,0)
    for idx, el in enumerate(mylist):
        if idx + 1 < len(mylist):
            next_el = mylist[idx + 1]
            if next_el - el == 1:
                one_occurr_agg.append(el)
            else:
                prev = mylist[idx - 1]
                if el - prev == 1 and idx != 1:
                    one_occurr_agg.append(el)
                if len(one_occurr_agg) > 0:
                    one_occurrences.append(one_occurr_agg)
                one_occurr_agg = []
    print(one_occurrences)
    print(count_arrangements(one_occurrences))

def main():
    input_list = list(sorted(read_input()))
    print(input_list)
    part_two(input_list)

main()