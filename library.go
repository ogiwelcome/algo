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
