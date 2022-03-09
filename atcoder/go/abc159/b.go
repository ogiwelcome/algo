package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	n := len(s)
	flg := true
	for i := 0; i < n/2; i++ {
		if s[i] != s[n-1-i] {
			flg = false
		}
		if s[i] != s[n/2-1-i] {
			flg = false
		}
		if s[n/2+1+i] != s[n-1-i] {
			flg = false
		}
	}
	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
