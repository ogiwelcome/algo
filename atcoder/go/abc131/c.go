package main

import (
	"fmt"
)

func main() {
	var a, b, c, d int64
	fmt.Scan(&a, &b, &c, &d)
	can_c := b/c - (a-1)/c
	can_d := b/d - (a-1)/d
	cd := c * d / gcd(c, d)
	can_cd := b/cd - (a-1)/cd
	cnt := can_c + can_d - can_cd
	ans := b - a + 1 - cnt
	fmt.Println(ans)
}

func gcd(a, b int64) int64 {
	for b != 0 {
		tmp := b
		b = a % b
		a = tmp
	}
	return a
}
