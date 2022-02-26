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
	h := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &h[i])
	}
	flg := true
	for i := n - 2; i >= 0; i-- {
		if h[i] > h[i+1]+1 {
			flg = false
		}
		if h[i] == h[i+1]+1 {
			h[i]--
		}
	}
	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
