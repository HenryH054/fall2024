import sys

def knapsack_recursive(capacity, weights, values, n, memo):
    if n == 0 or capacity == 0:
        return 0
    
    if (n, capacity) in memo:
        return memo[(n, capacity)]
    
    if weights[n - 1] > capacity:
        result = knapsack_recursive(capacity, weights, values, n - 1, memo)
    else:
        result = max(
            knapsack_recursive(capacity, weights, values, n - 1, memo),
            values[n - 1] + knapsack_recursive(capacity - weights[n - 1], weights, values, n - 1, memo)
        )
    
    memo[(n, capacity)] = result
    return result

def knapsack_solver(filename):
    with open(filename, 'r') as f:
        knapsack_size, n = map(int, f.readline().split())
        
        values, weights = [], []
        for line in f.readlines():
            value, weight = map(int, line.split())
            values.append(value)
            weights.append(weight)

    memo = {}
    
    return knapsack_recursive(knapsack_size, weights, values, n, memo)

filename = 'problem16.7.txt'
sys.setrecursionlimit(10000)
optimal_value = knapsack_solver(filename)
print("Optimal Value:", optimal_value)
