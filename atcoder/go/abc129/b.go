package main

import (
	"fmt"
)

func main() {
	var n int
	w := make([]int, n)
	s := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&w[i])
		s += w[i]
	}
	ans := s
	sw := 0
	for i := 0; i < n; i++ {
		sw += w[i]
		ans = min(ans, abs(sw-(s-sw)))
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}
func abs(v int) int {
	if v > 0 {
		return v
	} else {
		return -v
	}
}
