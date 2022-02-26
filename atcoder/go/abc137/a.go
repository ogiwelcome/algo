package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	ans := max(a+b, max(a-b, a*b))
	fmt.Println(ans)
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
