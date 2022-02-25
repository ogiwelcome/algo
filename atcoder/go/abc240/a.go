package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	if b-a == 1 || (a == 1 && b == 10) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
