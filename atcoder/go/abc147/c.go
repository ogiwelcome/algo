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
	x := make([][]int, n)
	y := make([][]int, n)
	for i := 0; i < n; i++ {
		var a int
		fmt.Fscan(r, &a)
		x[i] = make([]int, a)
		y[i] = make([]int, a)
		for j := 0; j < a; j++ {
			fmt.Fscan(r, &x[i][j], &y[i][j])
			x[i][j]--
		}
	}
	var ans int = 0
	for bit := 0; bit < (1 << n); bit++ {
		flg := true
		cnt := 0
		for i := 0; i < n; i++ {
			if (bit>>i)&1 == 1 {
				cnt++
				for j := 0; j < len(x[i]); j++ {
					if (bit>>x[i][j])&1 != y[i][j] {
						flg = false
					}
				}
			}
		}
		if flg && ans < cnt {
			ans = cnt
		}
	}
	fmt.Println(ans)
}
