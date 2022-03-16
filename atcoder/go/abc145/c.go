package main

import (
	"fmt"
	"math"
)

type pair struct {
	x int
	y int
}

func main() {
	var n int
	fmt.Scan(&n)
	var x, y int
	a := make([]pair, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x, &y)
		a[i] = pair{x, y}
	}
	var ans float64 = 0.0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			dx := a[i].x - a[j].x
			dy := a[i].y - a[j].y
			ans += math.Sqrt(float64(dx*dx + dy*dy))
		}
	}
	fmt.Println(ans / float64(n))
}
