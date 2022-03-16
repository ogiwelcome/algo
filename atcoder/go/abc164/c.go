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
	cnt := map[string]int{}
	for i := 0; i < n; i++ {
		var s string
		fmt.Fscan(r, &s)
		cnt[s]++
	}
	fmt.Println(len(cnt))
}
