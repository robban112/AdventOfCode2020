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

def part_one(mylist):
    pass

def main():
    part_one(input_list)

main()