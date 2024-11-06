v = [1, 2, 3, 4, 5]
w = [1, 3, 2, 5, 4]
n = 5 
W = 9 

m = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, W + 1):
        if w[i - 1] <= j:
            m[i][j] = max(m[i - 1][j], v[i - 1] + m[i - 1][j - w[i - 1]])
        else:
            m[i][j] = m[i - 1][j]


for row in m:
    print(row)


items = []
i = n
j = W

while i > 0 and j > 0:
    if m[i][j] != m[i - 1][j]:
        items.append(i - 1)
        j -= w[i - 1]
    i -= 1

items.reverse()
print("Selected items:", items)
