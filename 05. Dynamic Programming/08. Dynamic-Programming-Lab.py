'''
1. Dynamic Programming
контролиран brute forse за генериране на всички решения
problem -> subproblem -> subproblem

2. Fibonacci Sequence
  Fn = F(n-1) + F(n-2)
  optimization - memorization with list/dict

3. Move Down/Right sum


4. Longest Common Subsequence


5. Longest Increasing Subsequence


'''

#= = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Fibonacci - memorization
#= = = = = = = = = = = = = = = = = = = = = = = = =
def calc_fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
    memo[n] = result
    return result

n = int(input())
print(calc_fib(n, {}))

#= = = = = = = = = = = = = = = = = = = = = = = = = 
#02. Move Down/Right
#= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

rows = int(input())
cols = int(input())
matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col]

row = rows - 1
col = cols - 1
result = deque()

while row > 0 and col > 0:
    result.appendleft([row, col])
    if dp[row][col-1] >= dp[row-1][col]:
        col -= 1
    else:
        row -= 1

while row > 0:
    result.appendleft([row, col])
    row -= 1

while col > 0:
    result.appendleft([row, col])
    col -= 1

result.appendleft([0, 0])

print(*result, sep=' ')

#= = = = = = = = = = = = = = = = = = = = = = = = = 
#03. Longest Common Subsequence
#= = = = = = = = = = = = = = = = = = = = = = = = =
first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = list()
for _ in range(rows):
    dp.append([0] * cols)

for row in range(1,rows):
    for col in range(1,cols):
        if first[row-1] == second[col-1]:
            dp[row][col] = dp[row-1][col-1] + 1
        else:
            dp[row][col] = max(dp[row-1][col], dp[row][col-1])

print(dp[rows - 1][cols - 1])
# = = = = = EXTRA FUNCTIONALITY
row = rows - 1
col = cols - 1
result = list()

while row > 0 and col > 0:
    if first[row-1] == second[col-1]:
        result.append(first[row-1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col-1]:
        row -= 1
    else:
        col -= 1

print(list(reversed(result)))

#= = = = = = = = = = = = = = = = = = = = = = = = = 
#04. Longest Increasing Subsequence
#= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

nums = [int(x) for x in input().split()]

size = [0] * len(nums)
size[0] = 1
prev_ll = [None] * len(nums)
best_idx = 0
best_size = 1
for current in range(1,len(nums)):
    current_number = nums[current]
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        prev_number = nums[prev]

        if prev_number >= current_number:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    prev_ll[current] = current_parent

    if current_best_size > best_size:
        best_idx = current
        best_size = current_best_size

result = deque()

while best_idx is not None:
    result.appendleft(nums[best_idx])
    best_idx = prev_ll[best_idx]

print(*result, sep=' ')

#= = = = = = = = = = = = = = = = = = = = = = = = = 