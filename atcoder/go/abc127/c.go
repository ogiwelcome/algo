package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int
	re := bufio.NewReader(os.Stdin)
	fmt.Fscan(re, &n, &m)
	cnt := make([]int, n+2)
	var l, r int
	for i := 0; i < m; i++ {
		fmt.Fscan(re, &l, &r)
		cnt[l]++
		cnt[r+1]--
	}
	for i := 0; i < n; i++ {
		cnt[i+1] += cnt[i]
	}
	ans := 0
	for i := 1; i <= n; i++ {
		if cnt[i] == m {
			ans++
		}
	}
	fmt.Println(ans)
}
