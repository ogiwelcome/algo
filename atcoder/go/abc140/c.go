package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	b := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		fmt.Scan(&b[i])
	}
	a := make([]int, n)
	a[0] = b[0]
	for i := 1; i < n-1; i++ {
		a[i] = min(b[i], b[i-1])
	}
	a[n-1] = b[n-2]
	s := 0
	for i := 0; i < n; i++ {
		s += a[i]
	}
	fmt.Println(s)
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
