package main

import (
	"fmt"
)

func main() {
	var k int
	fmt.Scan(&k)
	ans := 0
	for a := 1; a <= k; a++ {
		for b := 1; b <= k; b++ {
			g1 := gcd(a, b)
			for c := 1; c <= k; c++ {
				ans += gcd(g1, c)
			}
		}
	}
	fmt.Println(ans)
}

func gcd(a, b int) int {
	for b > 0 {
		r := a % b
		a = b
		b = r
	}
	return a
}
