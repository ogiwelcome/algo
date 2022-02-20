package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type pair struct {
	a, b int
}

func main() {
	var r = bufio.NewReader(os.Stdin)
	var n, w int
	fmt.Fscan(r, &n, &w)
	ar := make([]pair, n)
	for i := range ar {
		fmt.Fscan(r, &ar[i].a, &ar[i].b)
	}
	sort.Slice(ar, func(i, j int) bool {
		return ar[i].a > ar[j].a
	})
	ans := 0
	for _, v := range ar {
		if v.b <= w {
			ans += v.a * v.b
			w -= v.b
		} else {
			ans += v.a * w
			w = 0
		}
	}
	fmt.Println(ans)
}
