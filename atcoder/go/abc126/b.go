package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var s string
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &s)
	s1, s2 := s[:2], s[2:]
	n1, _ := strconv.Atoi(s1)
	n2, _ := strconv.Atoi(s2)
	if 1 <= n1 && n1 <= 12 {
		if 1 <= n2 && n2 <= 12 {
			fmt.Println("AMBIGUOUS")
		} else {
			fmt.Println("MMYY")
		}
	} else {
		if 1 <= n2 && n2 <= 12 {
			fmt.Println("YYMM")
		} else {
			fmt.Println("NA")
		}
	}
}
