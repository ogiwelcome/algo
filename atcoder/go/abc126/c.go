package main

import (
	"fmt"
	"math"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	ans := 0.0
	for i := 1; i <= n; i++ {
		sc := i
		cnt := 0
		for sc < k {
			sc *= 2
			cnt++
		}
		ans += math.Pow(0.5, float64(cnt)) / float64(n)
	}
	fmt.Println(ans)
}
