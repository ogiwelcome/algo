package main

import (
	"fmt"
)

func main() {
	var n, a, b int
	fmt.Scan(&n, &a, &b)
	ans := min(n*a, b)
	fmt.Println(ans)
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
