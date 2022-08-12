= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Binomial Coefficients - меморизация(използване на cash)
= = = = = = = = = = = = = = = = = = = = = = = = =
def calc_binom(n, k, memo):
    key = f'{n} {k}'
    if key in memo:
        return memo[key]
    if n == 0 or k == 0 or n == k:
        return 1

    result = calc_binom(n-1, k-1, memo) + calc_binom(n-1, k, memo)
    memo[key] = result
    return result

n = int(input())
k = int(input())

print(calc_binom(n, k, {}))

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Word Differences
= = = = = = = = = = = = = = = = = = = = = = = = =
s1 = input()
s2 = input()

dp = list()
rows = len(s1) + 1
cols = len(s2) + 1
for _ in range(rows):
    dp.append([0] * (cols))

for col in range(1, cols):
    dp[0][col] = col

for row in range(1,rows):
    dp[row][0] = row

for row in range(1,rows):
    for col in range(1,cols):
        if s1[row-1] == s2[col-1]:
            dp[row][col] = dp[row-1][col-1]
        else:
            dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + 1

print(f'Deletions and Insertions: {dp[rows-1][cols-1]}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Connecting Cables (Longest Common Subsequence)
= = = = = = = = = = = = = = = = = = = = = = = = =
cables = [int(x) for x in input().split()]

size = len(cables) + 1
positions = [pos for pos in range(1, size)]

lcs = list()
for _ in range(size):
    lcs.append([0] * size)

for row in range(1,size):
    for col in range(1,size):
        if cables[row-1] == positions[col-1]:
            lcs[row][col] = lcs[row-1][col-1] + 1
        else:
            lcs[row][col] = max(lcs[row-1][col], lcs[row][col-1])

print(f'Maximum pairs connected: {lcs[size - 1][size - 1]}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Minimum Edit Distance
= = = = = = = = = = = = = = = = = = = = = = = = =
rep_cost = int(input())
ins_cost = int(input())
del_cost = int(input())
s1 = input()
s2 = input()

rows = len(s1) + 1
cols = len(s2) + 1

dp = list()
for _ in range(rows):
    dp.append([0] * (cols))

for col in range(1, cols):
    dp[0][col] = dp[0][col-1] + ins_cost

for row in range(1,rows):
    dp[row][0] = dp[row-1][0] + del_cost

for row in range(1,rows):
    for col in range(1,cols):
        if s1[row-1] == s2[col-1]:
            dp[row][col] = dp[row-1][col-1]
        else:
            dp[row][col] = min(dp[row][col-1] + ins_cost, dp[row-1][col] + del_cost, dp[row-1][col-1] + rep_cost)

print(f'Minimum edit distance: {dp[rows-1][cols-1]}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Longest String Chain (Longest Increasing Subsequence)
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

words = input().split()

size = [0] * len(words)
prev = [None] * len(words)

best_size = 0
best_idx = 0

for idx in range(len(words)):
    current_word = words[idx]
    current_size = 1
    parent = None

    for prev_idx in range(idx-1, -1, -1):
        prev_word = words[prev_idx]

        if len(prev_word) >= len(current_word):
            continue

        if size[prev_idx] + 1 >= current_size:
            current_size = size[prev_idx] + 1
            parent = prev_idx

    size[idx] = current_size
    prev[idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = idx

lis = deque()

idx = best_idx
while idx is not None:
    lis.appendleft(words[idx])
    idx = prev[idx]

print(*lis, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
06. Longest Zigzag Subsequence
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

nums = [int(x) for x in input().split()]

dp = list()
for _ in range(2):
    dp.append([0] * len(nums))
parent = list()
for _ in range(2):
    parent.append([None] * len(nums))

dp[0][0] = dp[1][0] = 1

best_size = 0
best_col = 0
best_row = 0

for current in range(1,len(nums)):
    current_number = nums[current]
    current_size = 1
    for prev in range(current-1, -1, -1):
        prev_number = nums[prev]

        if current_number > prev_number and dp[1][prev] + 1 >= dp[0][current]:
            dp[0][current] = dp[1][prev] + 1
            parent[0][current] = prev

        if current_number < prev_number and dp[0][prev] + 1 >= dp[1][current]:
            dp[1][current] = dp[0][prev] + 1
            parent[1][current] = prev

    if dp[0][current] > best_size:
        best_size = dp[0][current]
        best_row = 0
        best_col = current
    if dp[1][current] > best_size:
        best_size = dp[1][current]
        best_row = 1
        best_col = current

result = deque()
while best_col is not None:
    result.appendleft(nums[best_col])
    best_col = parent[best_row][best_col]
    best_row = 1 if best_row == 0 else 0


print(*result, sep=" ")

= = = = = = = = = = = = = = = = = = = = = = = = =