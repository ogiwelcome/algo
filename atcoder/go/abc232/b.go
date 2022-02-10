package main

import (
	"bytes"
	"fmt"
)

func main() {
	var ss, tt string
	fmt.Scan(&ss, &tt)
	s := []byte(ss)
	t := []byte(tt)
	for k := 0; k < 27; k++ {
		for i := 0; i < len(s); i++ {
			if s[i] == 'z' {
				s[i] = 'a'
			} else {
				s[i] += 1
			}
		}
		if bytes.Equal(s, t) {
			fmt.Println("Yes")
			return
		}
	}
	fmt.Println("No")
}
