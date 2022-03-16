package main

import (
	"fmt"
)

func main() {
	var a, b, c, d int
	fmt.Scan(&a, &b, &c, &d)
	flg := 1
	for a > 0 && c > 0 {
		if flg == 1 {
			c -= b
		} else {
			a -= d
		}
		flg = 1 - flg
	}
	if a <= 0 {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
	}
}
