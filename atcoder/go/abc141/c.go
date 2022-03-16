package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n, k, q int
	fmt.Scan(&n, &k, &q)
	sc := make([]int, n)
	for i := 0; i < n; i++ {
		sc[i] += k - q
	}
	for i := 0; i < q; i++ {
		var a int
		fmt.Fscan(r, &a)
		sc[a-1] += 1
	}
	for i := 0; i < n; i++ {
		if sc[i] > 0 {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	}
}
