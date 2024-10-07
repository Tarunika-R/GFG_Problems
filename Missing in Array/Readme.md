# Missing Element Finder

## Problem Description

Given an array `arr` of size `n−1` that contains distinct integers in the range of 1 to `n` (inclusive), find the missing element. The array is a permutation of size `n` with one element missing. Return the missing element.

### Examples

#### Example 1:
- **Input:** 
  - `n = 5`
  - `arr = [1, 2, 3, 5]`
- **Output:** 
  - `4`
- **Explanation:** 
  - All the numbers from 1 to 5 are present except 4.

#### Example 2:
- **Input:** 
  - `n = 2`
  - `arr = [1]`
- **Output:** 
  - `2`
- **Explanation:** 
  - All the numbers from 1 to 2 are present except 2.

### Constraints
- `1 ≤ n ≤ 10^5`
- `1 ≤ arr[i] ≤ n`

## Expected Time Complexity
- O(n)

## Expected Auxiliary Space
- O(1)

## Solution

### Approach

The problem can be solved using the formula for the sum of the first `n` natural numbers. The steps involved are:

1. **Calculate the expected sum**: The sum of the first `n` natural numbers is given by the formula `n * (n + 1) / 2`.
2. **Calculate the actual sum**: Sum all the elements in the given array `arr`.
3. **Find the missing element**: Subtract the actual sum from the expected sum.

### Algorithm

1. Compute the length of the array `arr` and add 1 to get `n` (since the array is of size `n-1`).
2. Calculate the expected sum using the formula for the sum of the first `n` natural numbers.
3. Calculate the sum of elements in the array.
4. The missing element is the difference between the expected sum and the actual sum.