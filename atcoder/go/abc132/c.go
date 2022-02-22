package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var n int
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n)
	d := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &d[i])
	}
	sort.Ints(d)
	cnt := d[n/2] - d[n/2-1]
	fmt.Println(cnt)
}
