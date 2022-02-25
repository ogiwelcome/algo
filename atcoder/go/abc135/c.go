package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var n int
	fmt.Fscan(r, &n)
	a := make([]int, n+1)
	b := make([]int, n)
	for i := 0; i < n+1; i++ {
		fmt.Fscan(r, &a[i])
	}
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &b[i])
	}
	cnt := 0
	for i := 0; i < n; i++ {
		if b[i] < a[i] {
			val := b[i]
			b[i] -= val
			a[i] -= val
			cnt += val
		} else {
			val := a[i]
			b[i] -= val
			a[i] -= val
			cnt += val
			if i < n-1 {
				val = min(a[i+1], b[i])
				a[i+1] -= val
				b[i] -= val
				cnt += val

			}
		}
	}
	if a[n] > 0 && b[n-1] > 0 {
		v := min(a[n], b[n-1])
		a[n] -= v
		b[n-1] -= v
		cnt += v
	}
	fmt.Fprintln(w, cnt)
}
func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
