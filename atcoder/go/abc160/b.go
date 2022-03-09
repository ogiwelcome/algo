package main

import (
	"fmt"
)

func main() {
	var x int
	fmt.Scan(&x)
	cnt := 0
	r := x / 500
	cnt += r * 2 * 500
	x -= r * 500
	r2 := x / 5
	cnt += r2 * 5
	fmt.Println(cnt)
}
