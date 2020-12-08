import numpy

input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(line.strip())

def is_in_list(element, _list):
    is_in_list = False
    for _, _list_el in _list:
        if element == _list_el:
            is_in_list = True
    return is_in_list

def is_in_list_2(element, _list):
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


def get_bag(mylist):
    bags = {}
    for line in mylist:
        sub_bag = []
        spaces = line.split(" ")
        counter = 4
        current_bag = spaces[0] + spaces[1]
        while len(spaces) > counter:
            if RepresentsInt(spaces[counter]):
                sub_bag.append((int(spaces[counter]), spaces[counter + 1] + spaces[counter + 2]))
            else:
                sub_bag.append('No bags')
            counter += 4
        bags[current_bag] = sub_bag
    return bags

def get_diff(bag_one, bag_two):
    diff = []
    for b in bag_one:
        if not is_in_list_2(b, bag_two):
            diff.append(b)
    return diff

def part_one(mylist):
    bags = get_bag(mylist)
    all_bags = []
    new_bags = ["shinygold"]
    while len(new_bags) > 0:
        sub_bags = contains_bags(bags, new_bags)
        new_bags = get_diff(sub_bags, all_bags)
        new_bags = list(set(new_bags))
        all_bags.append(new_bags)
    count = 0
    ibb = []
    for b in all_bags:
        for ib in b:
            ibb.append(ib)
    ibb = list(set(ibb))    
    print(len(ibb))

adding = 1

def part_two(mylist):
    bags = get_bag(mylist)
    current_bags = []
    print(get_length((1, 'shinygold'), bags))

def get_length(bag, bags):
    other_bags = bags[bag[1]]
    if other_bags[0] == 'No bags':
        return 0
    else:
        sum_bags = 0
        for other in other_bags:
            sum_bags += other[0] + (other[0] * get_length(other, bags))
        return sum_bags
    

def contains_bags(bags, contains):
    _contains = []
    for key in bags.keys():
        for c in contains:
            #print(c, bags[key], key)
            if is_in_list(c, bags[key]):
                _contains.append(key)
    return _contains

def main():
    part_two(input_list)

main()