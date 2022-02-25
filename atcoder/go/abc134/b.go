package main

import (
	"fmt"
)

func main() {
	var n, d int
	fmt.Scan(&n, &d)
	ans := (n + 2*d) / (2*d + 1)
	fmt.Println(ans)
}
