# Array Leaders

## Difficulty
Easy

## Problem Statement
Given an array `arr` of `n` positive integers, your task is to find all the leaders in the array. An element of the array is considered a leader if it is greater than all the elements on its right side or if it is equal to the maximum element on its right side. The rightmost element is always a leader.

## Examples

### Example 1
- **Input**: `n = 6 arr = [16, 17, 4, 3, 5, 2]`
- **Output**: `17 5 2`
- **Explanation**: There is nothing greater on the right side of 17, 5, and 2.

### Example 2
- **Input**: `n = 5 arr = [10, 4, 2, 4, 1]`
- **Output**: `10 4 4 1`
- **Explanation**: Both of the 4s are in output because an equal element is also allowed on the right side.

### Constraints
- `1 <= n <= 10^7`
- `0 <= arr[i] <= 10^7`

### Expected Time Complexity
- `O(n)`

### Expected Auxiliary Space
- `O(n)`

## Solution

To solve this problem efficiently, we can iterate through the array from right to left. By keeping track of the maximum element seen so far, we can identify leaders in a single pass. 