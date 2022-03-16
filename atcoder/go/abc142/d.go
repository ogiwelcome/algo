package main

import (
	"fmt"
)

func main() {
	var a, b int64
	fmt.Scan(&a, &b)
	g := gcd(a, b)
	// fmt.Println(g)
	var ans int64 = 1
	for i := int64(2); i <= 1000010; i++ {
		if g%i == 0 {
			ans++
			for g%i == 0 {
				g /= i
			}
		}
	}
	if g > 1 {
		ans++
	}
	fmt.Println(ans)
}
func gcd(x, y int64) int64 {
	for y != 0 {
		r := x % y
		x = y
		y = r
	}
	return x
}
