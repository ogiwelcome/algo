package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var r = bufio.NewReader(os.Stdin)
	var s, t string
	fmt.Fscan(r, &s, &t)
	if s == t {
		fmt.Println("Yes")
		return
	}
	c := []rune(s)
	for i := 0; i < len(s)-1; i++ {
		c[i], c[i+1] = c[i+1], c[i]
		if string(c) == t {
			fmt.Println("Yes")
			return
		}
		c[i], c[i+1] = c[i+1], c[i]
	}
	fmt.Println("No")
}
