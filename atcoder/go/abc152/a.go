package main

import (
	"fmt"
)

func main() {
	var n, m int
	fmt.Scan(&m, &n)
	if n == m {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
