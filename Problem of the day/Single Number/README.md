# Single Number

## Problem Description

Given an array `arr[]` of positive integers where every element appears an even number of times except for one. Find that number occurring an odd number of times.

### Examples:

#### Example 1:

- **Input**: `arr[] = [1, 1, 2, 2, 2]`
- **Output**: `2`
- **Explanation**: In the given array, all elements appear two times except for `2`, which appears three times.

#### Example 2:

- **Input**: `arr[] = [8, 8, 7, 7, 6, 6, 1]`
- **Output**: `1`
- **Explanation**: In the given array, all elements appear two times except for `1`, which appears only once.

## Expected Time Complexity:
- **O(n)**

## Expected Auxiliary Space:
- **O(1)**

## Constraints:
- `1 ≤ arr.size() ≤ 10^6`
- `0 ≤ arr[i] ≤ 10^5`

## Notes:
- The problem can be solved using bitwise XOR, where XORing all elements results in the number that appears an odd number of times.
