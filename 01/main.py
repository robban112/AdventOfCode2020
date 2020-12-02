import collections
import time

input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(int(line))


def find_sum(mylist):
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            for k in range(j + 1, len(mylist)):
                if int(mylist[i]) + int(mylist[j]) + int(mylist[k]) == 2020:
                    print(mylist[i])
                    print(mylist[j])
                    print(mylist[k])
                    print(int(mylist[i])*int(mylist[j])*int(mylist[k]))

def main():
    find_sum(input_list)
        
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