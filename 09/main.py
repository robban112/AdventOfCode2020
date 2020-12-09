import numpy

input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(int(line.strip()))

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

def is_sum_of_any_two(elem, elems):
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            if elems[i] + elems[j] == elem:
                return True
    return False

def part_one(mylist):
    preamble_length = 25
    preamble_agg = []
    for idx, elem in enumerate(mylist):
        if len(preamble_agg) >= preamble_length:
            if idx >= 5:
                #print("CONSIDER: " + str(elem))
                if not is_sum_of_any_two(elem, preamble_agg):
                    return (idx, elem)
            preamble_agg.pop(0)

        preamble_agg.append(elem)
        #print(preamble_agg)

def part_two(elems):
    (index, invalid_number) = part_one(elems)
    for i in range(index):
        list_agg = [elems[i]]
        for j in range(i+1, index):
            list_agg.append(elems[j])
            if numpy.sum(list_agg) == invalid_number:
                print(numpy.min(list_agg), numpy.max(list_agg))
                print(numpy.min(list_agg) + numpy.max(list_agg))


def main():
    #print(part_one(input_list))
    part_two(input_list)

main()