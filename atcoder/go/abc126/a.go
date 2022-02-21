package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var n, k int
	var s string
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n, &k, &s)
	ss := s[:k-1] + strings.ToLower(string(s[k-1])) + s[k:]
	fmt.Println(ss)
}
