package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const SAMPLE_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

type id_pair struct {
	lower int
	upper int
}

type aoc_answer struct {
	a int
	b int
}

func load_input(test bool) string {
	if test {
		return SAMPLE_INPUT
	}

	input, _ := os.ReadFile("../../data/2025/2")

	return string(input)
}

func parse_input(input string) []id_pair {
	pairs := strings.Split(input, ",")

	var res []id_pair

	for i := 0; i < len(pairs); i++ {
		pair := strings.Split(pairs[i], "-")
		lower, _ := strconv.ParseInt(pair[0], 0, 64)
		upper, _ := strconv.ParseInt(pair[1], 0, 64)

		res = append(res, id_pair{int(lower), int(upper)})
	}

	return res
}

func is_bad_a(i int) bool {
	l := int(math.Ceil(math.Log10(float64(i))))

	if l%2 == 1 {
		return false
	}

	mid := int(math.Pow10(l / 2))
	left := i / mid
	right := i % mid

	return left == right
}

func is_bad_b(i int) bool {
	s := strconv.Itoa(i)

	// OK SO GO DOESN'T DO FLIPPING BACKREFERENCES
	// imma come back to this
	match, _ := regexp.MatchString("^(\\d+)(\\1)+$", s)

	return match
}

func run(input []id_pair) aoc_answer {
	a := 0
	b := 0

	for i := 0; i < len(input); i++ {
		for j := input[i].lower; j <= input[i].upper; j++ {
			if is_bad_a(j) {
				a += j
			}
			if is_bad_b(j) {
				b += j
			}
		}
	}

	return aoc_answer{a, b}
}

func main() {
	input := parse_input(load_input(true))

	res := run(input)

	fmt.Printf("Part a: %v\n", res.a)
	fmt.Printf("Part b: %v\n", res.b)
}
