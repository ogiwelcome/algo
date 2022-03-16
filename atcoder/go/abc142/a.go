package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	if n%2 == 0 {
		fmt.Println(0.5)
	} else {
		k := (n + 1) / 2
		ans := float64(k) / float64(n)
		fmt.Println(ans)
	}
}
