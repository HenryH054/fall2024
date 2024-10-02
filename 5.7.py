import time
import random

def quicksortpivotmid(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortpivotmid(left) + middle + quicksortpivotmid(right)
    
def quicksortpivot0(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortpivot0(left) + middle + quicksortpivot0(right)
    
def quicksortpivotrand(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortpivotrand(left) + middle + quicksortpivotrand(right)

for y in range(100):

    rand_arr = []
    n=100
    for i in range(n):
        rand_arr.append(random.randint(1,9999))

    start_time = time.time()
    for x in range(10000):
        arr= rand_arr
        quicksortpivotmid(arr)
    print(f"Quick sort mid point pivot: {time.time() - start_time}")


    start_time = time.time()
    for x in range(10000):
        arr = rand_arr
        quicksortpivot0(arr)
    print(f"Quick sort 0 pivot: {time.time() - start_time}")

    start_time = time.time()
    for x in range(10000):
        arr = rand_arr
        quicksortpivotrand(arr)
    print(f"Quick sort random point pivot {time.time() - start_time}\n")
