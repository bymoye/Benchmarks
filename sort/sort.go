package main

import (
	"fmt"
	"math/rand"
	"time"
)

func bubleSort(array []int) []int {
	length := len(array)
	for i := 0; i < length; i++ {
		for j := 0; j < length-i-1; j++ {
			if array[j] > array[j+1] {
				array[j+1], array[j] = array[j], array[j+1]
			}
		}
	}
	return array
}
func main() {
	array := make([]int, 10000)
	for i := 0; i < len(array); i++ {
		array[i] = rand.Intn(1000)
	}
	startTime := time.Now()
	bubleSort(array)
	endTime := time.Since(startTime)
	fmt.Println(endTime)
}
