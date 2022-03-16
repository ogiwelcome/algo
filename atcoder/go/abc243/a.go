package main
import (
	"fmt"
)
func main() {
	var v,a,b,c int
	v%=a+b+c
	fmt.Scan(&v,&a,&b,&c)
	if v-a<0 {
		fmt.Println("F")
	} else if v-a-b<0 {
		fmt.Println("M")
	} else if v-a-b-c<0 {
		fmt.Println("T")
	}
}