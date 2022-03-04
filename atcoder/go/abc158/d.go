package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var s []byte
	fmt.Scan(&s)
	var q int
	fmt.Scan(&q)
	var sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	var mode int
	var hs, ts []byte
	for i := 0; i < q; i++ {
		sc.Scan()
		t, _ := strconv.Atoi(sc.Text())
		if t == 1 {
			mode = 1 - mode
		} else {
			sc.Scan()
			f, _ := strconv.Atoi(sc.Text())
			sc.Scan()
			c := []byte(sc.Text())[0]
			if mode == 0 {
				if f == 1 {
					hs = append(hs, c)
				} else {
					ts = append(ts, c)
				}
			} else {
				if f == 1 {
					ts = append(ts, c)
				} else {
					hs = append(hs, c)
				}
			}
		}
	}
	if mode == 0 {
		fmt.Printf("%s%s%s\n", string(reverse(hs)), string(s), string(ts))
	} else {
		fmt.Printf("%s%s%s\n", string(reverse(ts)), string(reverse(s)), string(hs))
	}
}

func reverse(bs []byte) []byte {
	nbs := make([]byte, len(bs))
	for i := range bs {
		nbs[i] = bs[len(bs)-1-i]
	}
	return nbs
}
