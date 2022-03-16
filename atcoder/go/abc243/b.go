package main
import (
	"fmt"
)
func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	b := make([]int, n)
	for i:=0;i<n;i++{
		fmt.Scan(&a[i])
	}
	for i:=0;i<n;i++{
		fmt.Scan(&b[i])
	}
	cnt1 := 0
	cnt2 := 0
	for i:=0;i<n;i++{
		if a[i]==b[i]{
			cnt1++
		}
		for j:=0;j<n;j++{
			if a[i]==b[j] && i!=j {
				cnt2++
			}
		}
	}
	fmt.Println(cnt1)
	fmt.Println(cnt2)
}