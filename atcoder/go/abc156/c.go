package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	x := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x[i])
	}
	var ans int = 1e9
	for i := 1; i <= 100; i++ {
		s := 0
		for j := 0; j < n; j++ {
			s += (i - x[j]) * (i - x[j])
		}
		if s < ans {
			ans = s
		}
	}
	fmt.Println(ans)
}
