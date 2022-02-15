package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	mn := s
	mx := s
	for i := 0; i < len(s); i++ {
		sft := s[1:] + s[0:1]
		if sft < mn {
			mn = sft
		}
		if sft > mx {
			mx = sft
		}
		s = sft
	}
	fmt.Print(mn, "\n", mx)
}
