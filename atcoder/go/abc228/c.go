package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var r = bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(r, &n, &k)
	ar := make([]int, n)
	br := make([]int, n)
	for i := range ar {
		var p1, p2, p3 int
		fmt.Fscan(r, &p1, &p2, &p3)
		ar[i] = p1 + p2 + p3
		br[i] = ar[i]
	}
	sort.Ints(br)
	for _, v := range ar {
		ans := "No"
		if v+300 >= br[n-k] {
			ans = "Yes"
		}
		fmt.Println(ans)
	}
}
