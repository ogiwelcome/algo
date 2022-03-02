package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	l := len(s)
	cnt := 0
	for i := 0; i < l/2; i++ {
		if s[i] != s[l-1-i] {
			cnt++
		}
	}
	fmt.Println(cnt)
}
