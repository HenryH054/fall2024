import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr, low, high)

def rselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = randomized_partition(arr, low, high)

    rank = pivot_index - low + 1

    if rank == k: 
        return arr[pivot_index]
    elif k < rank: 
        return rselect(arr, low, pivot_index - 1, k)
    else: 
        return rselect(arr, pivot_index + 1, high, k - rank)

arr = [10, 4, 5, 8, 6, 11, 26]
k = 3
result = rselect(arr, 0, len(arr) - 1, k)
print(f"The {k}rd smallest element is {result}")
