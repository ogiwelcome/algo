package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int
	fmt.Scan(&n)
	ans := 0
	for i := 1; i <= n; i++ {
		s := strconv.Itoa(i)
		if len(s)%2 == 1 {
			ans++
		}
	}
	fmt.Println(ans)
}
