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

def quicksortpivotrandofthree(arr):
    if len(arr) <= 1:
        return arr
    random_var = (random.randint(0, len(arr) - 1) + random.randint(0, len(arr) - 1) + random.randint(0, len(arr) - 1)) // 3
    pivot = arr[random_var]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortpivotrandofthree(left) + middle + quicksortpivotrandofthree(right)


runtime = [0,0,0,0]
for y in range(1000):

    rand_arr = []
    n=random.randint(100,5000)
    for i in range(n):
        rand_arr.append(random.randint(1,9999))

    start_time = time.time()
    for x in range(10):
        arr= rand_arr
        quicksortpivotmid(arr)
    runtime[0] += time.time() - start_time 


    start_time = time.time()
    for x in range(10):
        arr = rand_arr
        quicksortpivot0(arr)
    runtime[1] += time.time() - start_time 

    start_time = time.time()
    for x in range(10):
        arr = rand_arr
        quicksortpivotrand(arr)
    runtime[2] += time.time() - start_time 

    start_time = time.time()
    for x in range(10):
        arr = rand_arr
        quicksortpivotrandofthree(arr)
    runtime[3] += time.time() - start_time 

print(f"Midpoint: {runtime[0]/1000}\nZero: {runtime[1]/1000}\nRandom:{runtime[2]/1000}\n3Random: {runtime[3]/1000}")
