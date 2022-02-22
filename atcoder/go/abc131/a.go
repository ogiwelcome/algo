package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	flg := true
	for i := 0; i < 3; i++ {
		if s[i] == s[i+1] {
			flg = false
		}
	}
	if flg {
		fmt.Println("Good")
	} else {
		fmt.Println("Bad")
	}
}
