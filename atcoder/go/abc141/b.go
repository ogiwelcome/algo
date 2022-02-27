package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	flg := true
	for i := 0; i < len(s); i++ {
		if i%2 == 0 && s[i] == 'L' {
			flg = false
		}
		if i%2 == 1 && s[i] == 'R' {
			flg = false
		}
	}
	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
