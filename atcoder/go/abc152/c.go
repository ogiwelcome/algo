package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(r, &n)
	p := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &p[i])
	}
	cnt := 1
	v := p[0]
	for i := 1; i < n; i++ {
		if v > p[i] {
			cnt++
			v = p[i]
		}
	}
	fmt.Println(cnt)
}
