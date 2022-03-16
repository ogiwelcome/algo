package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	dx := a - b
	m := math.Pow(32, float64(dx))
	fmt.Printf("%d", int(m))
}
