package main

import (
	"fmt"
)

func main() {
	var n, m, x int
	fmt.Scan(&n, &m, &x)
	c := make([]int, n)
	a := make([][]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&c[i])
		a[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Scan(&a[i][j])
		}
	}
	ans := int(1e9)
	for bit := 0; bit < (1 << n); bit++ {
		sc := make([]int, m)
		money := 0
		for j := 0; j < n; j++ {
			if (bit>>j)&1 == 1 {
				money += c[j]
				for k := 0; k < m; k++ {
					sc[k] += a[j][k]
				}
			}
		}
		flg := true
		for j := 0; j < m; j++ {
			if sc[j] < x {
				flg = false
			}
		}
		if flg && ans > money {
			ans = money
		}
	}
	if ans == int(1e9) {
		fmt.Println(-1)
	} else {
		fmt.Println(ans)
	}
}
