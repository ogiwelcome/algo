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
	s := make([]string, n)
	anagrams := map[string]int{}
	ans := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &s[i])
		anagram := []rune(s[i])
		sort.Slice(anagram, func(i, j int) bool { return anagram[i] < anagram[j] })
		ans += anagrams[string(anagram)]
		anagrams[string(anagram)]++
	}
	fmt.Println(ans)

}
