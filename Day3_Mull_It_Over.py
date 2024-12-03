"""
Day 3 of Advent of Code 2024

Author: Jared Jones Pankhurst
Date: 03/12/2024

"""
import re


def calculate_mul_instructions(data):
    """Returns the sum of the products of each pair in the list"""
    running_sum = 0
    for item in data:
        running_sum += item[0] * item[1]

    return running_sum


def calculate_mul_instructions_part2(data):
    """Returns the sum of the products of each enabled pair in the list"""
    running_sum = 0
    enabled = True
    for item in data:
        if item == "don't()":
            enabled = False
            continue

        if item == "do()":
            enabled = True
            continue

        if enabled:
            running_sum += item[0] * item[1]
        
    return running_sum
        
    
def read_input_part2(filename):
    """Reads an input file into appropriate lists"""
    with open(filename) as file:
        file_contents = file.read()
        data = re.findall("([0-9]+,[0-9]+)|do\(\)|don't\(\)", file_contents)
        instructions = re.findall("do\(\)|don't\(\)", file_contents)

    clean_data = []
    index = 0
    for item in data:
        if 'mul({0})'.format(item) in file_contents:
            clean_data.append(tuple(map(int, item.split(','))))
        elif item == '':
            clean_data.append(instructions[index])
            index += 1

    return clean_data


def read_input_part1(filename):
    """Reads an input file into appropriate lists"""
    with open(filename) as file:
        file_contents = file.read()
        data = re.findall('([0-9]+,[0-9]+)', file_contents)

    clean_data = []
    for item in data:
        if 'mul({0})'.format(item) in file_contents:
            clean_data.append(tuple(map(int,item.split(','))))

    return clean_data


def main():
    """Main function of the program."""
    data = read_input_part2("Day3_input.txt")
    print('\n')
    print(data)
    print(calculate_mul_instructions_part2(data))

if __name__ == "__main__":
    main()