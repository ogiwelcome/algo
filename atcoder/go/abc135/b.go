package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	p := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&p[i])
	}
	ans := false
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			p[i], p[j] = p[j], p[i]
			flg := true
			for k := 0; k < n-1; k++ {
				if p[k] > p[k+1] {
					flg = false
				}
			}
			if flg {
				ans = true
			}
			p[i], p[j] = p[j], p[i]
		}
	}
	if ans {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
