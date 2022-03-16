package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(r, &n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
	}
	sort.Ints(a)
	ans := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			a1 := a[i]
			a2 := a[j]
			idx := sort.SearchInts(a, a1+a2)
			if idx <= j {
				continue
			} else {
				ans += idx - j - 1
			}
		}
	}
	fmt.Println(ans)
}
