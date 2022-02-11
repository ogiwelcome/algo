package main

import (
	"fmt"
)

func main() {
	var x int
	fmt.Scan(&x)
	if x >= 42 {
		fmt.Printf("AGC%03d\n", x+1)
	} else {
		fmt.Printf("AGC%03d\n", x)
	}
}
