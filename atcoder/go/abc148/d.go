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
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
	}
	now := 1
	for i := 0; i < n; i++ {
		if a[i] == now {
			now++
		}
	}
	now--
	if now == 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(n - now)
	}
}
