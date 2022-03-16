package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	r := bufio.NewReader(os.Stdin)
	a := make([]int, n+1)
	for i := 0; i < m; i++ {
		var tmp int
		fmt.Fscan(r, &tmp)
		a[tmp]++
	}
	dp := make([]int, n+1)
	dp[0] = 1
	mod := int(1e9 + 7)
	for i := 0; i < n; i++ {
		for j := i + 1; j <= min(i+2, n); j++ {
			if a[j] == 0 {
				dp[j] += dp[i]
				dp[j] %= mod
			}
		}
	}
	fmt.Println(dp[n])
}
func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
