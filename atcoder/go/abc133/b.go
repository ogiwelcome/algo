package main

import (
	"fmt"
	"math"
)

func main() {
	var n, d int
	fmt.Scan(&n, &d)
	x := make([][]int, n)
	for i := 0; i < n; i++ {
		x[i] = make([]int, d)
		for j := 0; j < d; j++ {
			fmt.Scan(&x[i][j])
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			c1 := 0
			for k := 0; k < d; k++ {
				c1 += (x[i][k] - x[j][k]) * (x[i][k] - x[j][k])
			}
			d := int(math.Sqrt(float64(c1)))
			if abs(c1-d*d) < 1 {
				ans++
			}
		}
	}
	fmt.Println(ans)
}

func abs(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}
