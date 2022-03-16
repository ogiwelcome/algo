package main

import (
	"fmt"
	"strconv"
)

func main() {
	var k int
	var x, y string
	fmt.Scan(&k, &x, &y)

	a, _ := strconv.ParseInt(x, k, 0)
	b, _ := strconv.ParseInt(y, k, 0)
	fmt.Println(a * b)
}
