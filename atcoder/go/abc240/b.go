package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	mp := make(map[int]int)
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		mp[a]++
	}
	fmt.Println(len(mp))
}
