package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	d := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&d[i])
	}
	ans := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			ans += d[i] * d[j]
		}
	}
	fmt.Println(ans)
}
