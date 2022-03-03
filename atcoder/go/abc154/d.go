package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(r, &n, &k)
	p := make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &p[i])
	}
	var ans float64 = -1
	var s float64 = 0
	for i := 0; i < k; i++ {
		s += (1 + p[i]) / 2.0
	}
	ans = max(ans, s)
	for i := k; i < n; i++ {
		s += (p[i]+1)/2.0 - (p[i-k]+1)/2.0
		ans = max(ans, s)
	}
	fmt.Println(ans)
}
func max(a, b float64) float64 {
	if a > b {
		return a
	} else {
		return b
	}
}
