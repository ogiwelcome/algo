package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int
	fmt.Scan(&n)
	ans := 0
	cnt := make([][]int, 10)
	for i := 0; i <= 9; i++ {
		cnt[i] = make([]int, 10)
	}
	for i := 1; i <= n; i++ {
		s := strconv.Itoa(i)
		s1, _ := strconv.Atoi(string(s[0]))
		s2, _ := strconv.Atoi(string(s[len(s)-1]))
		cnt[s1][s2]++
	}
	for i := 1; i <= 9; i++ {
		for j := 1; j <= 9; j++ {
			ans += cnt[i][j] * cnt[j][i]
		}
	}
	fmt.Println(ans)
}
