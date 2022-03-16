package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	r := bufio.NewReader(os.Stdin)
	a := make([]int, n)
	b := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
		b[i] = a[i]
	}
	sort.Ints(a)
	w := bufio.NewWriter(os.Stdout)
	for i := 0; i < n; i++ {
		if b[i] == a[n-1] {
			fmt.Fprintln(w, a[n-2])
		} else {
			fmt.Fprintln(w, a[n-1])
		}
	}
	w.Flush()
}
