package main

import (
	"fmt"
	"strconv"
)

func main() {
	var a, b, x int64
	fmt.Scan(&a, &b, &x)
	var l int64 = 0
	var r int64 = 1e9 + 1
	for r-l > 1 {
		mid := (l + r) / 2
		d := len(strconv.FormatInt(mid, 10))
		sc := a*mid + b*int64(d)
		if sc <= x {
			l = mid
		} else {
			r = mid
		}
	}
	fmt.Println(l)
}
