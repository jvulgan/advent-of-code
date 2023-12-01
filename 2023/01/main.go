/*
The newly-improved calibration document consists of lines of text; each line
originally contained a specific calibration value that the Elves now need to
recover. On each line, the calibration value can be found by combining the
first digit and the last digit (in that order) to form a single two-digit
number. It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid
"digits".
*/
package main

import (
	"bufio"
	"fmt"
	"os"
    "regexp"
    "strconv"
)
// function, which takes a string as
// argument and return the reverse of string.
func reverse(s string) string {
    rns := []rune(s) // convert to rune
    for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {

        // swap the letters of the string,
        // like first with last and so on.
        rns[i], rns[j] = rns[j], rns[i]
    }

    // return the reversed string.
    return string(rns)
}

func handleWordsAsNums(x string) string {
    num_word_to_digit := map[string]string{
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "eno": "1",
        "owt": "2",
        "eerht": "3",
        "ruof": "4",
        "evif": "5",
        "xis": "6",
        "neves": "7",
        "thgie": "8",
        "enin": "9",
    }
    _, err := strconv.Atoi(x)
    if err != nil {
        return num_word_to_digit[x]
    }
    return x
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
    // first part was solved with regex, for second there's potential for overlap
    // eighthree should return first: 8, last: 3
    // this was the fastest solution, don't @ me
    re_1 := regexp.MustCompile("[0-9]|one|two|three|four|five|six|seven|eight|nine")
    re_2 := regexp.MustCompile("[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin")
    var sum int
    var first, last string
	for scanner.Scan() {
        line := scanner.Text()
        if match := re_1.FindAllString(line, 1); match != nil {
            //fmt.Println(match)
            first = handleWordsAsNums(match[0])
        }
        if match := re_2.FindAllString(reverse(line), 1); match != nil {
            //fmt.Println(match)
            last = handleWordsAsNums(match[0])
        }
        //fmt.Println(line, first, last)
        num, _ := strconv.Atoi(first + last)
        sum += num
	}
    fmt.Print(sum)
}
