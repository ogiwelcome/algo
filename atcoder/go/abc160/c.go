package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var k, n int
	fmt.Fscan(r, &k, &n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
	}
	ans := a[n-1] - a[0]
	for i := 0; i < n-1; i++ {
		if ans > k-(a[i+1]-a[i]) {
			ans = k - (a[i+1] - a[i])
		}
	}
	fmt.Println(ans)
}
