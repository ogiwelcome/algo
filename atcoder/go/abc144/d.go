package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, x float64
	fmt.Scan(&a, &b, &x)
	if x > a*a*b/2.0 {
		var tmp float64 = math.Atan(2.0 * (a*a*b - x) / (a * a * a))
		fmt.Println(tmp * 180 / math.Pi)
	} else {
		var tmp float64 = math.Atan(a * b * b / x / 2.0)
		fmt.Println(tmp * 180 / math.Pi)
	}
}
