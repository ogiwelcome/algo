package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	flg := false
	for n > 0 {
		r := n % 10
		if r == 7 {
			flg = true
		}
		n /= 10
	}
	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
