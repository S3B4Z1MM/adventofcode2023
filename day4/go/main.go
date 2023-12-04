package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func splitInput(text string) (string, string, error) {
	splitText := strings.Split(text, ": ")
	numbersPart := strings.Split(splitText[1], "|")

	if len(numbersPart) < 2 {
		return "", "", fmt.Errorf("winning and guessing numbers not found")
	}

	winningNumbers := strings.TrimSpace(numbersPart[0])
	guessingNumbers := strings.TrimSpace(numbersPart[1])

	return winningNumbers, guessingNumbers, nil
}

func calculateTotalPoints(file_path string) (int, error) {
	file, err := os.Open(file_path)
	check(err)

	sc := bufio.NewScanner(file)

	points := 0

	for sc.Scan() {
		matchingNumbers := 0
		line := sc.Text()
		wn, gn, err := splitInput(line)
		if err != nil {
			return 0, err
		}

		for _, n := range strings.Fields(gn) {
			n = strings.TrimSpace(n)
			matched, _ := regexp.MatchString(`(^|\s)`+n+`($|\s)`, wn)
			if matched {
				matchingNumbers++
			}
		}

		if matchingNumbers == 0 {
			continue
		}

		points += 1 << (matchingNumbers - 1)
	}

	return points, nil
}

func main() {
	// Specify the file path for input.
	file_path := "../input.txt"

	// Print the results
	fmt.Println(calculateTotalPoints(file_path))
}
