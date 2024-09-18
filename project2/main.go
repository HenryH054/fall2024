package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	input := "problem3.5.txt"
	file, err := os.Open(input)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var data []int

	for scanner.Scan() {
		line, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic("Invalid input data")
		}
		data = append(data, line)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println("Inversions: ", invCount(data))
}

func merge(arr []int, left []int, right []int) int {
	i, j := 0, 0
	count := 0
	for k := 0; k < len(arr); k++ {
		if i >= len(left) {
			arr[k] = right[j]
			j++
		} else if j >= len(right) {
			arr[k] = left[i]
			i++
		} else if left[i] <= right[j] {
			arr[k] = left[i]
			i++
		} else {
			arr[k] = right[j]
			count += len(left) - i
			j++
		}
	}
	return count
}

func invCount(arr []int) int {
	if len(arr) < 2 {
		return 0
	}

	m := (len(arr)) / 2
	left := make([]int, m)
	right := make([]int, len(arr)-m)
	copy(left, arr[:m])
	copy(right, arr[m:])
	return invCount(left) + invCount(right) + merge(arr, left, right)
}
