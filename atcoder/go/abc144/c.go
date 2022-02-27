package main

import (
	"fmt"
)

func main() {
	var n int64
	fmt.Scan(&n)
	var ans int64 = 10000000000000
	for i := int64(1); i <= 1000000; i++ {
		if n%i == 0 {
			m := n / i
			if i+m-2 < ans {
				ans = i + m - 2
			}
		}
	}
	fmt.Println(ans)
}
