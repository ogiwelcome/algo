package main

import (
	"fmt"
)

func main() {
	var l float64
	fmt.Scan(&l)
	m := l / 3.0
	fmt.Println(m * m * m)
}
