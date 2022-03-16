package main

import (
	"fmt"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	h := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&h[i])
	}
	cnt := make([]int, n)
	var a, b int
	for i := 0; i < m; i++ {
		fmt.Scan(&a, &b)
		a--
		b--
		if h[a] > h[b] {
			cnt[b]++
		} else if h[a] < h[b] {
			cnt[a]++
		} else {
			cnt[a]++
			cnt[b]++
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		if cnt[i] == 0 {
			ans++
		}
	}
	fmt.Println(ans)
}
