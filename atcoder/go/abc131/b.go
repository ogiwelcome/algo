package main

import (
	"fmt"
)

func main() {
	var n, l int
	fmt.Scan(&n, &l)
	ans := int(10e10)
	s := int(10e10)
	for i := 0; i < n; i++ {
		v := abs(l + i)
		if v < s {
			s = v
			ans = n*(l-1) + n*(n+1)/2 - l - i
		}
	}
	fmt.Println(ans)
}
func abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -a
	}
}
