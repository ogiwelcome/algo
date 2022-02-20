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
	p := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &p[i])
	}
	q := make([]int, n)
	for i := 0; i < n; i++ {
		q[p[i]-1] = i + 1
	}
	for _, v := range q {
		fmt.Print(v)
		fmt.Print(" ")
	}
	fmt.Println()
}
