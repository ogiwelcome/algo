package main

import "fmt"

func main() {
	var s string
	mp := map[string]int{}
	fmt.Scan(&s)
	mp[s]++
	fmt.Scan(&s)
	mp[s]++
	fmt.Scan(&s)
	mp[s]++
	arr := []string{"ABC", "ARC", "AGC", "AHC"}
	for _, v := range arr {
		if mp[v] == 0 {
			fmt.Println(v)
			return
		}
	}
}
