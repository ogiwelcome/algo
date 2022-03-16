package main

import (
	"fmt"
)

func main() {
	var n, k, m int
	fmt.Scan(&n, &k, &m)
	a := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		fmt.Scan(&a[i])
	}
	s := 0
	for i := 0; i < n-1; i++ {
		s += a[i]
	}
	if m*n-s >= 0 && m*n-s <= k {
		fmt.Println(m*n - s)
	} else if m*n-s < 0 {
		fmt.Println(0)
	} else {
		fmt.Println(-1)
	}
}
