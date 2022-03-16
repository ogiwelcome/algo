package main

import (
	"fmt"
)

func main() {
	var n, x int
	fmt.Scan(&n, &x)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	cnt := 0
	mp := map[int]int{}
	for mp[x] == 0 {
		cnt++
		mp[x]++
		x = a[x-1]
	}
	fmt.Println(cnt)
}
