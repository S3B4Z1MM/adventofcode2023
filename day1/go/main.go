package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

// check is a utility function to handle errors. It panics if an error is not nil.
func check(e error) {
	if e != nil {
		panic(e)
	}
}

// part1 calculates and returns the calibration value based on the input file for part 1.
func part1(file_name string) int {
	calibration_value := 0

	file, err := os.Open(file_name)
	check(err)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		ptr := 0

		// Find the first digit in the line.
		for !unicode.IsDigit(rune(line[ptr])) {
			ptr += 1
		}

		// Convert the first digit character to its integer value.
		c1 := rune(line[ptr]) - 48
		ptr = len(line) - 1

		// Find the last digit in the line.
		for !unicode.IsDigit(rune(line[ptr])) {
			ptr -= 1
		}

		// Convert the last digit character to its integer value.
		c2 := rune(line[ptr]) - 48

		calibration_value += int(c1)*10 + int(c2)
	}

	file.Close()

	return calibration_value
}

// part2 calculates and returns the calibration value based on the input file for part 2.
func part2(file_name string) int {
	calibration_value := 0

	// Define a mapping from digit strings to their integer values.
	digit_strings := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
		"zero":  0,
	}

	file, err := os.Open(file_name)
	check(err)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		ptr := 0
		d := -1
		found := false

		// Find the first digit in the line using digit strings.
		for !unicode.IsDigit(rune(line[ptr])) && !found {
			for digit := range digit_strings {
				if ptr+len(digit) > len(line) {
					continue
				}
				if string(line[ptr:ptr+len(digit)]) == digit {
					d = digit_strings[digit]
					found = true
				}
			}
			ptr += 1
		}

		// Convert the first digit character to its integer value.
		c1 := rune(line[ptr]) - 48
		if d != -1 {
			c1 = rune(d)
		}

		ptr = len(line) - 1
		d = -1
		found = false

		// Find the last digit in the line using digit strings.
		for !unicode.IsDigit(rune(line[ptr])) && !found {
			for digit := range digit_strings {
				if ptr+len(digit) > len(line) {
					continue
				}
				if string(line[ptr:ptr+len(digit)]) == digit {
					d = digit_strings[digit]
					found = true
				}
			}
			ptr -= 1
		}

		// Convert the last digit character to its integer value.
		c2 := rune(line[ptr]) - 48
		if d != -1 {
			c2 = rune(d)
		}

		calibration_value += int(c1)*10 + int(c2)
	}

	file.Close()

	return calibration_value
}

func main() {
	// Specify the file path for input.
	file_path := "../input.txt"

	// Print the results
	fmt.Println("Part 1:", part1(file_path))
	fmt.Println("Part 2:", part2(file_path))
}
