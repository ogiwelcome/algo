package main

import (
	"fmt"
)

func main() {
	var n, x int
	fmt.Scan(&n, &x)
	l := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&l[i])
	}
	ans := 1
	sc := 0
	idx := 0
	for idx < n && sc+l[idx] <= x {
		ans++
		sc += l[idx]
		idx++
	}

	fmt.Println(ans)
}
