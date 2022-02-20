package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	fmt.Scan(&n)
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanLines)
	ans := make(map[string]int, n)
	for i := 0; i < n; i++ {
		sc.Scan()
		s := sc.Text()
		ans[s]++
	}
	fmt.Println(len(ans))
}
