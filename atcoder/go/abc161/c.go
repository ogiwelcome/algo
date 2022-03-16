package main

import (
	"fmt"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	r := n % k
	fmt.Println(min(r, k-r))
}
func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
