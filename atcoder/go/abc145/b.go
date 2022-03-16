package main

import (
	"fmt"
)

func main() {
	var n int
	var s string
	fmt.Scan(&n, &s)
	if n%2 == 0 {
		m := n / 2
		flg := true
		for i := 0; i < m; i++ {
			if s[i] != s[i+m] {
				flg = false
			}
		}
		if flg {
			fmt.Println("Yes")
			return
		}
	}
	fmt.Println("No")
}
