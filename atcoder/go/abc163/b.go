package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n, &m)
	a := make([]int, m)
	s := 0
	for i := 0; i < m; i++ {
		fmt.Fscan(r, &a[i])
		s += a[i]
	}
	if s <= n {
		fmt.Println(n - s)
	} else {
		fmt.Println(-1)
	}
}
