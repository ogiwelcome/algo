package main

import (
	"fmt"
)

func main() {
	var n, k int64
	fmt.Scan(&n, &k)
	mod := int64(1e9 + 7)
	var ans int64 = 0
	for i := k; i <= n+1; i++ {
		l := i * (i - 1) / 2
		r := n*i - l
		ans += r - l + 1
		ans %= mod
	}
	fmt.Println(ans)
}
