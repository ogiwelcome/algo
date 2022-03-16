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
	var a int
	cnt := make([]int, n)
	for i := 0; i < n-1; i++ {
		fmt.Fscan(r, &a)
		cnt[a-1]++
	}
	for i := 0; i < n; i++ {
		fmt.Println(cnt[i])
	}
}
