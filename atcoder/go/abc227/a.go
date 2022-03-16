package main

import (
	"fmt"
)

func main() {
	var n, k, a int
	fmt.Scan(&n, &k, &a)
	k += a - 1
	fmt.Println(((k - 1) % n) + 1)
}
