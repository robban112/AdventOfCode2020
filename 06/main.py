import numpy

input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(line.strip())

def count_group(group):
    print("count " + group)
    return len(list(set(group)))

def count_group_two(group, group_count):
    count = 0
    for char in list(set(group)):
        if group.count(char) == group_count:
            count += 1
    return count

def part_one(mylist):
    mylist.append("")
    group = ""
    count = 0
    for line in mylist:
        if line == "":
            count += count_group(group)
            group = ""
            continue
        group += line
    print(count)

def part_two(mylist):
    mylist.append("")
    group = ""
    group_count = 0
    count = 0
    for line in mylist:
        if line == "":
            count += count_group_two(group, group_count)
            group = ""
            group_count = 0
            continue
        group_count += 1
        group += line
    print(count)

def main():
    part_two(input_list)

main()