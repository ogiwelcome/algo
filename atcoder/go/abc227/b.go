package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	s := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&s[i])
	}
	flg := make([]int, n)
	for a := 1; a <= 250; a++ {
		for b := 1; b <= 250; b++ {
			x := 4*a*b + 3*a + 3*b
			for i := 0; i < n; i++ {
				if s[i] == x {
					flg[i] = 1
				}
			}
		}
	}
	cnt := 0
	for i := 0; i < n; i++ {
		if flg[i] == 0 {
			cnt++
		}
	}
	fmt.Println(cnt)
}
