import numpy
import collections 
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

def getValue(line):
    spaces = line.split(" ")
    _acc = spaces[1]
    int_acc = int(_acc[1:])
    if _acc[0] == '+':
        return int_acc
    else:
        return -1 * int_acc

def part_one(mylist):
    acc = 0
    shouldContinue = True
    currentLine = 0
    lines = []
    while shouldContinue:
        line = mylist[currentLine]
        spaces = line.split(" ")
        instruction = spaces[0]
        if instruction == 'nop':
            currentLine += 1
            pass
        elif instruction == 'acc':
            acc += getValue(line)
            currentLine += 1
        elif instruction == 'jmp':
            currentLine += getValue(line)
            if is_in_list(currentLine, lines):
                shouldContinue = False
        lines.append(currentLine)
    print(acc)

def is_infinite(instructions):
    shouldContinue = True
    currentLine = 0
    lines = []
    acc = 0
    while shouldContinue:
        if currentLine > len(instructions) - 1:
            return (False, acc)
        line = instructions[currentLine]
        spaces = line.split(" ")
        instruction = spaces[0]
        if instruction == 'nop':
            currentLine += 1
            pass
        elif instruction == 'acc':
            acc += getValue(line)
            currentLine += 1
        elif instruction == 'jmp':
            currentLine += getValue(line)
            if is_in_list(currentLine, lines):
                shouldContinue = False
        lines.append(currentLine)
    return (True, acc)

def part_one(mylist):
    acc = 0
    shouldContinue = True
    currentLine = 0
    lines = []
    while shouldContinue:
        line = mylist[currentLine]
        spaces = line.split(" ")
        instruction = spaces[0]
        if instruction == 'nop':
            currentLine += 1
            pass
        elif instruction == 'acc':
            acc += getValue(line)
            currentLine += 1
        elif instruction == 'jmp':
            currentLine += getValue(line)
            if is_in_list(currentLine, lines):
                shouldContinue = False
        lines.append(currentLine)
    print(acc)

def part_two(mylist):
    for idx, line in enumerate(mylist):
        spaces = line.split(" ")
        instruction = spaces[0]
        if instruction == 'nop':
            copy_list = mylist.copy()
            value = getValue(line)
            new_instruction = "jmp " + spaces[1]
            copy_list[idx] = new_instruction
            (infinite, acc) = is_infinite(copy_list)
            if not infinite:
                return acc
        elif instruction == 'jmp':
            copy_list = mylist.copy()
            value = getValue(line)
            new_instruction = "nop " + spaces[1]
            copy_list[idx] = new_instruction
            (infinite, acc) = is_infinite(copy_list)
            if not infinite:
                return acc


def main():
    print(part_two(input_list))

main()