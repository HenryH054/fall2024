contents = ""

with open("problem17.8nw.txt") as file:
    contents = file.readlines()

len_X, len_Y = contents[0].split()
len_X, len_Y = int(len_X), int(len_Y)
gap_cost, mismatch_cost = contents[1].split()
gap_cost, mismatch_cost = int(gap_cost), int(mismatch_cost)
X = contents[2].strip()
Y = contents[3].strip()

matrix = [[0] * (len_Y + 1) for _ in range(len_X + 1)]

for i in range(1, len_X + 1):
    matrix[i][0] = matrix[i - 1][0] + gap_cost
for j in range(1, len_Y + 1):
    matrix[0][j] = matrix[0][j - 1] + gap_cost

for i in range(1, len_X + 1):
    for j in range(1, len_Y + 1):
        match_or_mismatch = matrix[i - 1][j - 1] + (0 if X[i - 1] == Y[j - 1] else mismatch_cost)
        insert = matrix[i][j - 1] + gap_cost
        delete = matrix[i - 1][j] + gap_cost
        matrix[i][j] = min(match_or_mismatch, insert, delete)

nw_score = matrix[len_X][len_Y]

i, j = len_X, len_Y
aligned_X, aligned_Y = "", ""
while i > 0 or j > 0:
    current_score = matrix[i][j]
    if i > 0 and j > 0 and current_score == matrix[i - 1][j - 1] + (0 if X[i - 1] == Y[j - 1] else mismatch_cost):
        aligned_X = X[i - 1] + aligned_X
        aligned_Y = Y[j - 1] + aligned_Y
        i -= 1
        j -= 1
    elif i > 0 and current_score == matrix[i - 1][j] + gap_cost:
        aligned_X = X[i - 1] + aligned_X
        aligned_Y = "*" + aligned_Y
        i -= 1
    else:
        aligned_X = "*" + aligned_X
        aligned_Y = Y[j - 1] + aligned_Y
        j -= 1

print("NW Score:", nw_score)
print("Aligned Sequence X:", aligned_X)
print("Aligned Sequence Y:", aligned_Y)
