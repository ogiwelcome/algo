package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	flg := false
	for i := 1; i <= 9; i++ {
		if n%i == 0 {
			x := n / i
			if 1 <= x && x <= 9 {
				flg = true
			}
		}
	}
	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
