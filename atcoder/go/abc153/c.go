package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(r, &n, &k)
	h := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &h[i])
	}
	sort.Ints(h)
	ans := 0
	for i := 0; i < min(n, n-k); i++ {
		ans += h[i]
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
