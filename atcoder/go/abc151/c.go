package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(r, &n, &m)
	var p int
	var s string
	ac := map[int]bool{}
	cnt := map[int]int{}
	for i := 0; i <= n; i++ {
		ac[i] = false
		cnt[i] = 0
	}
	ac_cnt := 0
	wa_cnt := 0
	for i := 0; i < m; i++ {
		fmt.Fscan(r, &p, &s)
		val := ac[p]
		if val {
			continue
		} else {
			if s == "WA" {
				cnt[p]++
			} else {
				ac_cnt++
				wa_cnt += cnt[p]
				ac[p] = true
			}
		}
	}
	fmt.Println(ac_cnt, wa_cnt)
}
