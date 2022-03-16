package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	x := make([]int, n)
	y := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x[i], &y[i])
	}
	ans := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				x1 := x[j] - x[i]
				x2 := x[k] - x[i]
				y1 := y[j] - y[i]
				y2 := y[k] - y[i]
				if x1*y2-x2*y1 != 0 {
					ans++
				}
			}
		}
	}
	fmt.Println(ans)
}
