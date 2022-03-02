package main

import (
	"fmt"
)

func main() {
	var h, a int
	fmt.Scan(&h, &a)
	ans := (h + a - 1) / a
	fmt.Println(ans)
}
