package main

import (
	"fmt"
)

func main() {
	var a, b, c, k int64
	fmt.Scan(&a, &b, &c, &k)
	if k <= a {
		fmt.Println(k)
	} else if a <= k && k <= a+b {
		fmt.Println(a)
	} else {
		fmt.Println(a - (k - a - b))
	}
}
