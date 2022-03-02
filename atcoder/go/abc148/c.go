package main

import (
	"fmt"
)

func main() {
	var a, b int64
	fmt.Scan(&a, &b)
	g := gcd(a, b)
	ans := a * b / g
	fmt.Println(ans)
}
func gcd(a, b int64) int64 {
	for b > 0 {
		var r int64 = a % b
		a = b
		b = r
	}
	return a
}
