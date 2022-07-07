1. Algorithmic Complexity
    Worst-case - upper bound on the running time
    Average-case
    Best-case

    Asymptotic notations
        Big O - O(f(n))
        Big Theta - O(f(n))
        Big Omega - Om(f(n))
        
- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
2. Recursion
   - function calling itself
   - should have a base case
   - each step of the recursion should move towards the base case

    A. Types
        - direct recursion
        - indirec recursion
    B. Parts of recursion:
        - Pre-actions
        - Recursive calls
        - Post-actions
- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
3. Backtracking - class of algorithms for finding all solutions
    - The 8 Queens Problem
    - Finding All Paths in a Labyrinth Recusively

- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
4. Recursion or Iteration
A. Recursion
    - recursive calls are shower, but good for branching problems
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
B. Iteration
    - no function call cost
    - creates local variables
    - good for linear problems (no branching)
def fact(n):
    result = 1
    for i in range(1, n+1):
        result += id
    return result
    
    
    
    
    
- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
    
= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Recursive Array Sum
= = = = = = = = = = = = = = = = = = = = = = = = =
def array_sum(ll, idx):                     #
    if idx == len(ll) - 1:                  # Base case
        return ll[idx]                      # Base case
    return ll[idx] + array_sum(ll, idx + 1) # Recursive call

ll = [int(x) for x in input().split()]

print(array_sum(ll, 0))

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Recursive Factorial
= = = = = = = = = = = = = = = = = = = = = = = = =
def factoriel(n):                   #
    if n == 0:                      # Base case
        return 1                    # Base case
    return n * factoriel(n-1)       # Recursive call

n = int(input())
print(factoriel(n))

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Recursive Drawing
= = = = = = = = = = = = = = = = = = = = = = = = =
def recursive_drawing(n):
    if n == 0:
        return
    print('*' * n)
    recursive_drawing(n-1)
    print('#' * n)

n = int(input())
recursive_drawing(n)

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Generating 0/1 Vectors
= = = = = = = = = = = = = = = = = = = = = = = = =
def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for i in range(0, 2):
        vector[idx] = i
        gen01(idx + 1, vector)

n = int(input())
vector = [0] * n

gen01(0, vector)

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Paths in Labyrinth
= = = = = = = = = = = = = = = = = = = = = = = = =
def find_all_paths(row, col, lab, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return

    if lab[row][col] == '*':
        return

    if lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    else:
        lab[row][col] = 'v'
        find_all_paths(row-1, col, lab, 'U', path)
        find_all_paths(row+1, col, lab, 'D', path)
        find_all_paths(row, col-1, lab, 'L', path)
        find_all_paths(row, col+1, lab, 'R', path)
        lab[row][col] = '-'

    path.pop()

rows = int(input())
cols = int(input())
lab = []
for _ in range(rows):
    lab.append(list(input()))

find_all_paths(0, 0, lab, '', [])

= = = = = = = = = = = = = = = = = = = = = = = = = 
06. 8 Queens Puzzle
= = = = = = = = = = = = = = = = = = = = = = = = =
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def can_place_queen(row, col, board, rows, cols, left_diag, right_diag):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row-col) in left_diag:
        return False
    if (row+col) in right_diag:
        return False
    return True

def set_queen(row, col, board, rows, cols, left_diag, right_diag):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diag.add(row-col)
    right_diag.add(row+col)

def remove_queen(row, col, board, rows, cols, left_diag, right_diag):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diag.remove(row-col)
    right_diag.remove(row+col)

def put_queens(row, col, board, rows, cols, left_diag, right_diag):
    if row == 8:
        print_board(board)
        return

    for col in range(8):
        if can_place_queen(row, col, board, rows, cols, left_diag, right_diag):
            set_queen(row, col, board, rows, cols, left_diag, right_diag)
            put_queens(row+1, col, board, rows, cols, left_diag, right_diag)
            remove_queen(row, col, board, rows, cols, left_diag, right_diag)

n = 8
board = []
[board.append(['-']*n) for _ in range(8)]
put_queens(0, 0, board, set(), set(), set(), set())

= = = = = = = = = = = = = = = = = = = = = = = = = 
07. Recursive Fibonacci 
= = = = = = = = = = = = = = = = = = = = = = = = =
def fibonachi(n):
    fib0 = 1
    fib1 = 1
    for _ in range(n-1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

n = int(input())
print(fibonachi(n))
= = = = = = = = = = = = = = = = = = = = = = = = = 