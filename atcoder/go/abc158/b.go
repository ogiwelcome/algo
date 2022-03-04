package main

import (
	"fmt"
)

func main() {
	var n, a, b int64
	fmt.Scan(&n, &a, &b)
	c := n / (a + b)
	ans := n - c*(a+b)
	ans2 := c*a + min(ans, a)
	fmt.Println(ans2)
}
func min(a, b int64) int64 {
	if a > b {
		return b
	} else {
		return a
	}
}
