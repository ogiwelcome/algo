package main

import (
	"fmt"
)

func main() {
	var w, h, x, y int
	fmt.Scan(&w, &h, &x, &y)
	flg := 0
	if x*2 == w && y*2 == h {
		flg = 1
	}
	ans := float64(w) * float64(h) / 2.0
	fmt.Println(ans, flg)
}
func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
