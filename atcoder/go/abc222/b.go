package main

import (
	"fmt"
)

func main() {
	var n, p int
	fmt.Scan(&n, &p)
	var cnt int
	scores := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&scores[i])
		if scores[i] < p {
			cnt += 1
		}
	}
	fmt.Println(cnt)
}
