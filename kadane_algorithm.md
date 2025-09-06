# Kadane's Algorithm

Kadane's Algorithm is used to find the **maximum sum subarray** in a given 1D array of integers (both positive and negative). It works in **O(n)** time, which is optimal compared to brute-force approaches.

---

## Intuition

- We want the contiguous subarray with the largest sum.
- Keep track of the **current maximum sum ending at the current position** (`current_sum`).
- Keep track of the **global maximum sum found so far** (`max_sum`).
- If `current_sum` becomes negative, reset it to `0` (since negative sums reduce future sums).

---

## Algorithm Steps

1. Initialize:
```python
max_sum = float('-inf')
current_sum = 0
```
2. Loop through the array:
```python
for num in array:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)
```
3. Return `max_sum`.

---

## Example

Input: `[−2, 1, −3, 4, −1, 2, 1, −5, 4]`  

Step-by-step:

| i | num | current_sum | max_sum |
|---|-----|-------------|---------|
| 0 | -2  | -2          | -2      |
| 1 | 1   | 1           | 1       |
| 2 | -3  | -2          | 1       |
| 3 | 4   | 4           | 4       |
| 4 | -1  | 3           | 4       |
| 5 | 2   | 5           | 5       |
| 6 | 1   | 6           | 6       |
| 7 | -5  | 1           | 6       |
| 8 | 4   | 5           | 6       |

**Output:** `6` (subarray `[4, -1, 2, 1]`)

---

## Python Implementation

```python
def kadane(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadane(arr))  # Output: 6
```

---

## Time and Space Complexity

- **Time Complexity:** `O(n)` — Single pass through the array  
- **Space Complexity:** `O(1)` — Only two variables are used

