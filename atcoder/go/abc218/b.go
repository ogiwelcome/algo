package main

import (
	"fmt"
)

func main() {
	p := make([]int, 26)
	for i := 0; i < 26; i++ {
		fmt.Scan(&p[i])
	}
	for i := 0; i < 26; i++ {
		fmt.Printf("%c", p[i]+96)
	}
}
