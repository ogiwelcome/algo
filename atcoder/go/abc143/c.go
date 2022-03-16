package main

import (
	"fmt"
)

func main() {
	var n int
	var s string
	fmt.Scan(&n, &s)
	ans := 0
	for i := 0; i < len(s)-1; i++ {
		if s[i] != s[i+1] {
			ans++
		}
	}
	fmt.Println(ans + 1)
}
