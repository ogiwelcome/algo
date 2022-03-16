package main

import (
	"fmt"
)

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	flg := true
	if a == b && a == c {
		flg = false
	} else if a != b && b != c && a != c {
		flg = false
	}
	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
