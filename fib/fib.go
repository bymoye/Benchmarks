package main

import (
	"fmt"
	"time"
)

func fib_rec(n int) int {
	if n == 1 || n == 2 {
		return 1
	}
	return fib_rec(n-1) + fib_rec(n-2)
}
func main() {
	startTime := time.Now()
	fib_rec(30)
	endTime := time.Since(startTime)
	fmt.Println(endTime)
}
