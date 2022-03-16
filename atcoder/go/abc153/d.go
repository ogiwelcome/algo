package main

import (
	"fmt"
)

func main() {
	var h int64
	fmt.Scan(&h)
	fmt.Println(f(h))
}

func f(x int64) int64 {
	if x == 1 {
		return 1
	} else {
		return f(x/2)*2 + 1
	}
}
