import collections
import time
import numpy

input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(line.strip())


def parse_input(mylist):
    M = len(mylist[0])
    N = len(mylist) + 20
    matrix_trees = [ [ 0 for i in range(M) ] for j in range(N) ]
    for idx_one, line in enumerate(mylist):
        for idx_two, char in enumerate(line):
            matrix_trees[idx_one][idx_two] = char
    return matrix_trees

def count_trees(matrix_trees, right_slope, down_slope):
    count = 0
    right = 0
    down = 0

    while down < len(matrix_trees):
        count += 1 if matrix_trees[down][right] == '#' else 0
        down += down_slope
        right += right_slope
        right = right % len(matrix_trees[0])
    return count

def part_one(mylist):
    matrix_trees = parse_input(mylist)
    print(count_trees(matrix_trees, 3, 1))

def part_two(mylist):
    sum_list = []
    matrix_trees = parse_input(mylist)
    sum_list.append(count_trees(matrix_trees, 3, 1))
    sum_list.append(count_trees(matrix_trees, 1, 1))
    sum_list.append(count_trees(matrix_trees, 5, 1))
    sum_list.append(count_trees(matrix_trees, 7, 1))
    sum_list.append(count_trees(matrix_trees, 1, 2))
    print((numpy.prod(sum_list)))

def main():
    part_one(input_list)
    part_two(input_list)


main()