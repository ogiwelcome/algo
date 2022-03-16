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
	flg := true
	for i := 0; i < n-1; i++ {
		if a[i] == a[i+1] {
			flg = false
		}
	}
	if flg {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
