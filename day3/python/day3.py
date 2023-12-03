import re
import string


def read_input(filename='day3/input.txt'):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def find_symbols_and_gears(lines):
    gears = {}

    for row in range(len(lines)):
        for col in range(len(lines[row])):

            # Check if the character is not a digit or dot
            current_char = lines[row][col]
            if current_char not in f'{string.digits}.':
                gears[(row, col)] = []

    return gears


def process_symbols_and_gears(lines, gears):
    p1_total = 0

    for row_num, row in enumerate(lines):
        for match in re.finditer(r'\d+', row):
            possibilities = []

            # Generate positions around the matched digits
            for i in range(match.start() - 1, match.end() + 1):
                possibilities.extend([(row_num - 1, i), (row_num, i), (row_num + 1, i)])

            found = False

            # Check if the positions are in the gears dictionary and update gears
            for pos in possibilities:
                if pos in gears:
                    found = True
                    gears[pos].append(int(match.group()))

            if found:
                p1_total += int(match.group())

    return p1_total, gears


def calculate_part_two(gears):
    p2_total = 0
    for g in gears:
        # Check if a position in gears has exactly 2 values and calculate the product
        if len(gears[g]) == 2:
            p2_total += (gears[g][0] * gears[g][1])
    return p2_total


def main():
    lines = read_input()
    gears = find_symbols_and_gears(lines)
    p1_total, gears = process_symbols_and_gears(lines, gears)
    
    print('Part One -', p1_total)

    p2_total = calculate_part_two(gears)
    print('Part Two -', p2_total)

if __name__ == "__main__":
    main()
