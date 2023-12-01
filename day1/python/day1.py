import os
import string

digits = string.digits

def part1():
    finalDigits = 0
    with open('day1/input.txt') as inputFile:
        for line in inputFile:
            foundDigits = ''
            for char in line.strip():
                if char in digits:
                    foundDigits += ''.join(char)

            if len(foundDigits) > 2:
                tmp = f'{foundDigits[0]}{foundDigits[-1]}'
                finalDigits += int(tmp)
            elif len(foundDigits) == 1:
                tmp = f'{foundDigits}{foundDigits}'
                finalDigits += int(tmp)
            else:
                finalDigits += int(foundDigits)
    
    return finalDigits

if __name__ == '__main__':
    print(part1())