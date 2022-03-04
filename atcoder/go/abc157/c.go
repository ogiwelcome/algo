package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	ss := make([]int, n)
	for i := 0; i < n; i++ {
		ss[i] = -1
	}
	for i := 0; i < m; i++ {
		var s, c int
		fmt.Scan(&s, &c)
		if ss[s-1] != -1 && ss[s-1] != c {
			fmt.Println(-1)
			return
		} else {
			ss[s-1] = c
		}
	}
	if ss[0] == 0 && n > 1 {
		fmt.Println(-1)
		return
	}
	if ss[0] == -1 {
		if n == 1 {
			ss[0] = 0
		} else {
			ss[0] = 1
		}
	}
	for i := 1; i < n; i++ {
		if ss[i] == -1 {
			ss[i] = 0
		}
	}
	ans := ""
	for i := 0; i < n; i++ {
		ans += strconv.Itoa(ss[i])
	}
	fmt.Println(ans)
}
