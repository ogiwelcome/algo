package main

import (
	"fmt"
)

func main() {
	var n, k, r, s, p int
	var st string
	fmt.Scan(&n, &k, &r, &s, &p, &st)
	l := len(st)
	ans := 0
	for i := 0; i < k; i++ {
		idx := i
		cnt := 0
		for idx+k < l {
			if st[idx] == st[idx+k] {
				cnt++
			} else {
				if st[idx] == 'r' {
					ans += p * (cnt/2 + 1)
				} else if st[idx] == 'p' {
					ans += s * (cnt/2 + 1)
				} else {
					ans += r * (cnt/2 + 1)
				}
				cnt = 0
			}
			idx += k
		}
		if st[idx] == 'r' {
			ans += p * (cnt/2 + 1)
		} else if st[idx] == 'p' {
			ans += s * (cnt/2 + 1)
		} else {
			ans += r * (cnt/2 + 1)
		}
	}
	fmt.Println(ans)
}
