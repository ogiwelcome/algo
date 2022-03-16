package main

import (
	"fmt"
)

func main() {
	a := make([][]int, 3)
	for i := 0; i < 3; i++ {
		a[i] = make([]int, 3)
		for j := 0; j < 3; j++ {
			fmt.Scan(&a[i][j])
		}
	}
	var n int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var b int
		fmt.Scan(&b)
		for j := 0; j < 3; j++ {
			for k := 0; k < 3; k++ {
				if b == a[j][k] {
					a[j][k] = -1
				}
			}
		}
	}
	for i := 0; i < 3; i++ {
		flg := true
		for j := 0; j < 3; j++ {
			if a[i][j] != -1 {
				flg = false
			}
		}
		if flg {
			fmt.Println("Yes")
			return
		}
		flg = true
		for j := 0; j < 3; j++ {
			if a[j][i] != -1 {
				flg = false
			}
		}
		if flg {
			fmt.Println("Yes")
			return
		}
		flg = true
		for j := 0; j < 3; j++ {
			if a[j][j] != -1 {
				flg = false
			}
		}
		if flg {
			fmt.Println("Yes")
			return
		}
		flg = true
		for j := 0; j < 3; j++ {
			if a[2-j][j] != -1 {
				flg = false
			}
		}
		if flg {
			fmt.Println("Yes")
			return
		}
	}
	fmt.Println("No")
}
