package main

import (
	"fmt"
)

func main() {
	var s, t, x int
	ans := "No"
	fmt.Scan(&s, &t, &x)
	if s <= t && x < t {
		ans = "Yes"
	} else if t < s && (x < t || s <= x) {
		ans = "Yes"
	}
	fmt.Println(ans)
}
