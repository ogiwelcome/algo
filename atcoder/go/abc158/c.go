package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	for i := 1; i <= 100000; i++ {
		var x float64 = math.Floor(float64(i) * 0.08)
		var y float64 = math.Floor(float64(i) * 0.10)
		if x == a && y == b {
			fmt.Println(i)
			return
		}

	}
	fmt.Println(-1)
}
