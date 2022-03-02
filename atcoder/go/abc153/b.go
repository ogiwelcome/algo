package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var h, n int
	fmt.Fscan(r, &h, &n)
	a := make([]int, n)
	s := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
		s += a[i]
	}
	if s >= h {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
