package main

import (
	"fmt"
	"strconv"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	s1 := strconv.Itoa(a)
	s2 := strconv.Itoa(b)
	if a <= b {
		for i := 0; i < b; i++ {
			fmt.Print(s1)
		}
	} else {
		for i := 0; i < a; i++ {
			fmt.Print(s2)
		}
	}
	fmt.Print("\n")
}
