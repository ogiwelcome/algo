package main

import (
	"fmt"
	"math"
)

func main() {
	var p, q, r float64
	fmt.Scan(&p, &q, &r)
	ans := math.Min(p+q, math.Min(p+r, q+r))
	fmt.Println(int(ans))
}
