package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	var r = bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n)
	a := make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
	}
	var x int64
	fmt.Fscan(r, &x)
	s := int64(0)
	for i := 0; i < n; i++ {
		s += a[i]
	}
	t := x / s
	ans := t * int64(n)
	tot := t * s
	i := 0
	for tot <= x {
		tot += a[i]
		i++
		ans++
	}
	fmt.Println(ans)
}
