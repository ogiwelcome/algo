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
	cnt := map[int]int{}
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
		cnt[a[i]]++
	}
	s := 0
	for i := 1; i <= n; i++ {
		c := cnt[i]
		s += c * (c - 1) / 2
	}
	for i := 0; i < n; i++ {
		c := cnt[a[i]]
		ds := -c*(c-1)/2 + (c-1)*(c-2)/2
		fmt.Println(s + ds)
	}
}
