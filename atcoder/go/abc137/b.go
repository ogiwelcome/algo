package main

import (
	"fmt"
)

func main() {
	var k, x int
	fmt.Scan(&k, &x)
	left := max(-1000000, x-k+1)
	right := min(1000000, x+k-1)
	for i := left; i <= right; i++ {
		fmt.Print(i)
		if i < right {
			fmt.Print(" ")
		}
	}
	fmt.Print("\n")
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
