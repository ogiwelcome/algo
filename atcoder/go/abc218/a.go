package main

import (
	"fmt"
)

func main() {
	var s string
	var n int
	fmt.Scan(&n, &s)
	if s[n-1] == 'o' {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
