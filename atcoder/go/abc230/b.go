package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	t := "oxxoxxoxxoxxoxxoxxoxxoxx"
	if strings.Count(t, s) > 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
