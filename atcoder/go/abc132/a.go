package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	flg := false
	if s[0] == s[1] && s[2] == s[3] && s[0] != s[2] {
		flg = true
	} else if s[0] == s[2] && s[1] == s[3] && s[0] != s[1] {
		flg = true
	} else if s[0] == s[3] && s[1] == s[2] && s[0] != s[1] {
		flg = true
	}
	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
