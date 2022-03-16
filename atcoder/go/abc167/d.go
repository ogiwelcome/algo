package main

import (
	"fmt"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	point := 0
	cnt := 0
	vis := make([]int, n)
	for rep := 0; rep < k; rep++ {
		vis[point] = cnt
		cnt++
		point = a[point] - 1
		if vis[point] != 0 {
			break
		}
	}
	k = (k - cnt) % (cnt - vis[point])
	for rep := 0; rep < k; rep++ {
		point = a[point] - 1
	}
	fmt.Println(point + 1)
}
