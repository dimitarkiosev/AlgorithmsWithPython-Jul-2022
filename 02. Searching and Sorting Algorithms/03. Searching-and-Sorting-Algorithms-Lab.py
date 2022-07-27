1. Searching Algorithms
  A. definition
  B. Type of searching
    -search for sub-structures
    -search for min/max
  C. Type algorithms
    - Linear Search - checking every one of the elements

ll = [1, 2, 3, 4, 5, 6, 7, 9]
target = 5
for idx, el in enumerate(ll):
    if el == target:
        print(idx)
        break
        
    - Binary Search - finds item in ordered data
    each step compare middle element

2. Simple Sorting Algotithms
    Classification
        complexity
            worst
            average
            best-case
        Type
            recursive
            stability - stable/not-stable
            comparison-based
        
    A. Selection Sort - swap the first with MIN el on the right, then second, etc, O(n2)
    
    B. Bubble Sort - swap to neighbor el when not in order until sorted, O(n2)
    
    C. Insertion Sort - move the first unsorted element left to its place, O(n2)
    
3. Advanced Sorting Algorithms
    - QuickSort
    - MergeSort

= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Binary Search
= = = = = = = = = = = = = = = = = = = = = = = = =
def binary_search(ll, target):
    left = 0
    right = len(ll) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = ll[mid_idx]

        if mid_el == target:
            return mid_idx

        if target > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1

ll = [int(x) for x in input().split()]
target = int(input())

print(binary_search(ll, target))

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Selection Sort
= = = = = = = = = = = = = = = = = = = = = = = = =
ll = [int(x) for x in input().split()]

for idx in range(len(ll)):
    min_el = ll[idx]
    min_idx = idx

    for next_idx in range(idx+1, len(ll)):
        next_el = ll[next_idx]
        if next_el < min_el:
            min_el = next_el
            min_idx = next_idx
    ll[idx], ll[min_idx] = ll[min_idx], ll[idx]

print(*ll, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Bubble Sort
= = = = = = = = = = = = = = = = = = = = = = = = =
#- - - - - - - - - -
#Bubble Sort 1
#- - - - - - - - - -
ll = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True
    for idx in range(1, len(ll) - counter):
        if ll[idx] < ll[idx-1]:
            ll[idx-1], ll[idx] = ll[idx], ll[idx-1]
            is_sorted = False
    counter += 1

print(*ll, sep=' ')
#- - - - - - - - - -
#Bubble Sort 2
#- - - - - - - - - -
ll = [int(x) for x in input().split()]

for i in range(len(ll)):
    for j in range(1, len(ll) - i):
        if ll[j-1] > ll[j]:
            ll[j], ll[j-1] = ll[j-1], ll[j]
            
print(*ll, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Insertion Sort
= = = = = = = = = = = = = = = = = = = = = = = = =
ll = [int(x) for x in input().split()]

for i in range(1, len(ll)):
    for j in range(i, 0, -1):
        if ll[j] < ll[j-1]:
            ll[j], ll[j-1] = ll[j-1], ll[j]
            
print(*ll, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Quicksort
= = = = = = = = = = = = = = = = = = = = = = = = =
def quick_sort(start, end, ll):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        if ll[left] > ll[pivot] > ll[right]:
            ll[left], ll[right] = ll[right], ll[left]
            
        if ll[left] <= ll[pivot]:
            left += 1
        if ll[right] >= ll[pivot]:
            right -= 1
            
    ll[pivot], ll[right] = ll[right], ll[pivot]
    quick_sort(start, right - 1, ll)
    quick_sort(left, end, ll)

ll = [int(x) for x in input().split()]

quick_sort(0, len(ll)-1, ll)
            
print(*ll, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
06. Merge Sort
= = = = = = = = = = = = = = = = = = = = = = = = =
def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left):
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right):
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return result

def merge_sort(ll):
    if len(ll) == 1:
        return ll

    mid_idx = len(ll) // 2
    left = ll[:mid_idx]
    right = ll[mid_idx:]

    return merge_arrays(merge_sort(left), merge_sort(right))

ll = [int(x) for x in input().split()]
ll_sorted = merge_sort(ll)
print(*ll_sorted, sep=' ')
= = = = = = = = = = = = = = = = = = = = = = = = = 