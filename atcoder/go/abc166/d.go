package main

import (
	"fmt"
)

func main() {
	var x int64
	fmt.Scan(&x)
	var a, b int64
	for a = -130; a <= 130; a++ {
		for b = -130; b <= 130; b++ {
			if a*a*a*a*a-b*b*b*b*b == x {
				fmt.Println(a, b)
				return
			}
		}
	}
}
