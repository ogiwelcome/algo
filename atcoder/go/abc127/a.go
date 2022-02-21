package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	if 6 <= a && a <= 12 {
		b /= 2
	} else if a <= 5 {
		b = 0
	}
	fmt.Println(b)
}
