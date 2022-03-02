package main

import (
	"fmt"
)

func main() {
	var a, b, k int64
	fmt.Scan(&a, &b, &k)
	if a >= k {
		a -= k
	} else {
		k -= a
		a = 0
		b -= min(k, b)
	}
	fmt.Println(a, b)
}
func min(a, b int64) int64 {
	if a > b {
		return b
	} else {
		return a
	}
}
