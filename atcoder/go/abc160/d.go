package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n, x, y int
	fmt.Fscan(r, &n, &x, &y)
	x -= 1
	y -= 1
	cnt := map[int]int{}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			var d int
			if x <= i && j <= y {
				d = min(j-i, i-x+1+y-j)
			} else if i <= x && j <= y {
				d = min(j-i, x-i+1+y-j)
			} else if x <= i && y <= j {
				d = min(j-i, i-x+j-y+1)
			} else if i <= x && y <= j {
				d = min(j-i, x-i+1+j-y)
			}
			cnt[d]++
		}
	}
	for i := 1; i <= n-1; i++ {
		fmt.Println(cnt[i])
	}
}
func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
