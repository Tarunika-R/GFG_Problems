# Sort 0s, 1s, and 2s

## Problem Statement

Given an array `arr` containing only 0s, 1s, and 2s, sort the array in ascending order.

### Examples:

1. **Input:** `arr[] = [0, 2, 1, 2, 0]`
   - **Output:** `[0, 0, 1, 2, 2]`
   - **Explanation:** The 0s, 1s, and 2s are segregated into ascending order.

2. **Input:** `arr[] = [0, 1, 0]`
   - **Output:** `[0, 0, 1]`
   - **Explanation:** The 0s, 1s, and 2s are segregated into ascending order.

3. **Input:** `arr[] = [2, 2, 2]`
   - **Output:** `[2, 2, 2]`
   - **Explanation:** Only 2s are present here.

### Constraints:

- \(1 \leq \text{arr.size()} \leq 10^6\)
- \(0 \leq \text{arr[i]} \leq 2\)