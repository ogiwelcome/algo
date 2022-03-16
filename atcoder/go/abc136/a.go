package main

import (
	"fmt"
)

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	if b+c <= a {
		fmt.Println(0)
	} else {
		fmt.Println(b + c - a)
	}
}
