package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	mp := make(map[string]int)
	idx := make([]string, n)
	for i := 0; i < n; i++ {
		var s string
		var p int
		fmt.Scan(&s, &p)
		s += string(100 - p)
		mp[s] = i + 1
		idx[i] = s
	}
	sort.Strings(idx)
	for _, s := range idx {
		fmt.Println(mp[s])
	}
}
