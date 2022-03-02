package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(r, &n)
	g := make([][]int, n)
	a := make([]int, n-1)
	b := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		fmt.Fscan(r, &a[i], &b[i])
		a[i]--
		b[i]--
		g[a[i]] = append(g[a[i]], i)
		g[b[i]] = append(g[b[i]], i)
	}
	col := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		col[i] = 0
	}
	var dfs func(x, pre int)
	dfs = func(x, pre int) {
		nxt := 0
		for _, id := range g[x] {
			y := a[id]
			if y == x {
				y = b[id]
			}
			if col[id] == 0 {
				nxt++
				if pre == nxt {
					nxt++
				}
				col[id] = nxt
				dfs(y, col[id])
			}
		}
	}
	dfs(0, -1)
	ans := 1
	for _, c := range col {
		if ans < c {
			ans = c
		}
	}
	fmt.Println(ans)
	for _, c := range col {
		fmt.Println(c)
	}
}
