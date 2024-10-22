# Second Largest Element in Array

## Problem Statement

Given an array `arr`, return the second largest element from the array. If the second largest element doesn't exist, then return `-1`.

### Note:
- The second largest element should not be equal to the first largest.

### Examples:

1. **Input:** arr = [12, 35, 1, 10, 34, 1]
   - **Output:** 34
   - **Explanation:** The largest element of the array is 35 and the second largest element is 34.

2. **Input:** arr = [10, 10]
   - **Output:** -1
   - **Explanation:** The largest element of the array is 10 and the second largest element does not exist.

### Constraints:
- 2 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5

## Solution

### Approach:
- Use two variables to track the largest and second largest elements in the array.
- Traverse the array and update these variables based on the conditions:
  - If the current element is greater than the largest element, update the second largest to be the largest and the largest to be the current element.
  - If the current element is greater than the second largest but less than the largest, update the second largest to be the current element.