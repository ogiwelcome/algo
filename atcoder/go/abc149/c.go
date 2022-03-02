package main

import (
	"fmt"
)

func main() {
	var x int
	fmt.Scan(&x)
	not_p := map[int]bool{}
	for i := 2; i <= 1e6; i++ {
		_, ok := not_p[i]
		if !ok {
			if i >= x {
				fmt.Println(i)
				return
			}
			for j := i + i; j <= 1e6; j += i {
				not_p[j] = true
			}
		}
	}
}
