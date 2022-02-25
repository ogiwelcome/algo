package main

import (
	"fmt"
)

func main() {
	var n, x int
	fmt.Scan(&n, &x)
	dp := make([]int, x+1)
	dp[0] = 1
	for i := 0; i < n; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		ndp := make([]int, x+1)
		for j := 0; j < x; j++ {
			if dp[j] == 1 {
				if j+a <= x {
					ndp[j+a] = 1
				}
				if j+b <= x {
					ndp[j+b] = 1
				}
			}
		}
		dp = ndp
	}
	if dp[x] == 1 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
