package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	if 2*b >= a {
		fmt.Println(0)
	} else {
		fmt.Println(a - 2*b)
	}
}
