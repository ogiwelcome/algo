package main

import (
	"fmt"
)

const MOD int64 = 1000000007

func mpow(a, x int64, mod int64) int64 {
	var res int64 = 1
	for ; x > 0; x >>= 1 {
		if x&1 == 1 {
			res *= a
			res %= mod
		}
		a *= a
		a %= mod
	}
	return res
}

func main() {
	var x, y int64
	fmt.Scan(&x, &y)
	if 2*y-x >= 0 && 2*x-y >= 0 && (2*y-x)%3 == 0 && (2*x-y)%3 == 0 {
		s := (2*y - x) / 3
		t := (2*x - y) / 3
		f := make([]int64, 2000010)
		f[0] = int64(1)
		for i := int64(1); i < 2000010; i++ {
			f[i] = (f[i-1] * i) % MOD
		}
		ans := f[s+t] * mpow(f[s], MOD-2, MOD) % MOD * mpow(f[t], MOD-2, MOD) % MOD
		fmt.Println(ans)
	} else {
		fmt.Println(0)
	}
}
