package main

import (
	"fmt"
)

func main() {
	var k int
	fmt.Scan(&k)
	que := make([]int, 0)
	for i := 1; i <= 9; i++ {
		que = append(que, i)
	}
	cnt := 0
	for len(que) > 0 {
		x := que[0]
		que = que[1:]
		cnt++
		if cnt == k {
			fmt.Println(x)
			return
		}
		d := x % 10
		for i := d - 1; i <= d+1; i++ {
			if 0 <= i && i <= 9 {
				que = append(que, 10*x+i)
			}
		}
	}
}
