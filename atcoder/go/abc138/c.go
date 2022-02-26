package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	v := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&v[i])
	}
	sort.Ints(v)
	ans := float64(v[0])
	for i := 1; i < n; i++ {
		ans = (ans + float64(v[i])) / 2.0
	}
	fmt.Println(ans)
}
