package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int64
	var r = bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n)
	res := ""
	for n != 0 {
		if n%2 != 0 {
			res = "A" + res
		}
		res = "B" + res
		n /= 2
	}
	fmt.Println(res)
}
