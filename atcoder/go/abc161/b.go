package main

import (
	"fmt"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	a := make([]int, n)
	sa := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
		sa += a[i]
	}
	cnt := 0
	for i := 0; i < n; i++ {
		if 4*m*a[i] >= sa {
			cnt++
		}
	}
	if cnt >= m {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
