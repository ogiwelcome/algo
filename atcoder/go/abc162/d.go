package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	var s string
	fmt.Scan(&s)
	ans := 0
	r := make([]int, n)
	g := make([]int, n)
	b := make([]int, n)
	if s[0] == 'R' {
		r[0]++
	} else if s[0] == 'G' {
		g[0]++
	} else {
		b[0]++
	}
	for i := 1; i < n; i++ {
		r[i] = r[i-1]
		g[i] = g[i-1]
		b[i] = b[i-1]
		if s[i] == 'R' {
			r[i]++
		} else if s[i] == 'G' {
			g[i]++
		} else {
			b[i]++
		}
	}
	for i := 0; i < n; i++ {
		if s[i] == 'R' {
			ans += g[i] * b[i]
		} else if s[i] == 'G' {
			ans += r[i] * b[i]
		} else {
			ans += r[i] * g[i]
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if j+2*i < n {
				x := j
				y := j + i
				z := j + 2*i
				if s[x] != s[y] && s[x] != s[z] && s[y] != s[z] {
					ans--
				}
			}
		}
	}
	fmt.Println(ans)
}
