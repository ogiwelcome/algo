package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	v := -1
	for _, val := range cnt {
		v = max(v, val)
	}
	res := []string{}
	for key, val := range cnt {
		if val == v {
			res = append(res, key)
		}
	}
	sort.Strings(res)
	for i := range res {
		fmt.Println(res[i])
	}

}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
