package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	c := 0.0
	for i := 0; i < n; i++ {
		c += 1 / float64(a[i])
	}
	fmt.Println(1.0 / c)
}
