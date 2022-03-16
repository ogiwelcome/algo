package main

import (
	"fmt"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	cnt := make([]int, n)
	var d, a int
	for rep := 0; rep < k; rep++ {
		fmt.Scan(&d)
		for i := 0; i < d; i++ {
			fmt.Scan(&a)
			cnt[a-1]++
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
