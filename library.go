package library

import ()

// stringのpermutation取得
func permutation(str string, first bool) []string {
	var res []string
	if len(str) == 1 {
		return append(res, str)
	}
	var strSet map[string]bool
	if first {
		strSet = make(map[string]bool)
	}
	for i := 0; i < len(str); i++ {
		strCopy := str[:i] + str[i+1:]
		for _, s := range permutation(strCopy, false) {
			if first {
				ss := string(str[i]) + s
				if _, ok := strSet[ss]; !ok {
					strSet[ss] = true
					res = append(res, ss)
				}
			} else {
				res = append(res, string(str[i])+s)
			}
		}
	}
	return res
}

// mod pow
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
