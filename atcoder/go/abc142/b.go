package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, k int
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n, &k)
	h := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &h[i])
	}
	cnt := 0
	for i := 0; i < n; i++ {
		if h[i] >= k {
			cnt++
		}
	}
	fmt.Println(cnt)
}
