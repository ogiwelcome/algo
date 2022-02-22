package main

import (
	"fmt"
)

func main() {
	var l, r int
	fmt.Scan(&l, &r)
	if r-l >= 2019 {
		fmt.Println(0)
	} else {
		ans := 2020
		for i := l; i <= r; i++ {
			for j := i + 1; j <= r; j++ {
				ii := i % 2019
				jj := j % 2019
				sc := (ii * jj) % 2019
				ans = min(ans, sc)
			}
		}
		fmt.Println(ans)
	}
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
