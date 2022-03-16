package main

import (
	"fmt"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	cnt := 0
	for n > 0 {
		cnt++
		n /= k
	}
	fmt.Println(cnt)
}
