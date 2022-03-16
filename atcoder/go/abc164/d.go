package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var s string
	fmt.Fscan(r, &s)
	rs := []rune(s)
	n := len(s)
	a := make([]int, n+1)
	b := 1
	for i := n - 1; i >= 0; i-- {
		a[i] = int(rs[i]-rune('0'))*b + a[i+1]
		a[i] %= 2019
		b *= 10
		b %= 2019
	}
	cnt := make([]int64, 2020)
	for i := 0; i < n+1; i++ {
		cnt[a[i]]++
	}
	var ans int64 = 0
	for i := 0; i <= 2018; i++ {
		c := cnt[i]
		ans += c * (c - 1) / 2
	}
	fmt.Println(ans)
}
