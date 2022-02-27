package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	cnt := 0
	x := 1
	for x < b {
		x = x + a - 1
		cnt++
	}
	fmt.Println(cnt)
}
