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
	mp := make(map[int]int, n)
	for i, v := range a {
		mp[v-1] = i + 1
	}
	for i := 0; i < n; i++ {
		fmt.Print(mp[i], " ")
	}
}
