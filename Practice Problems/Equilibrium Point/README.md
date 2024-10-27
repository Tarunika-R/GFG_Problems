# Equilibrium Point

## Problem Statement

Given an array `arr` of non-negative numbers, the task is to find the first equilibrium point in the array. The equilibrium point in an array is an index (or position) such that the sum of all elements before that index is the same as the sum of elements after it.

**Note:** Return the equilibrium point in 1-based indexing. Return -1 if no such point exists.

## Examples

1. **Input:** `arr[] = [1, 3, 5, 2, 2]`
   - **Output:** `3`
   - **Explanation:** The equilibrium point is at position 3 as the sum of elements before it (1+3) equals the sum of elements after it (2+2).

2. **Input:** `arr[] = [1]`
   - **Output:** `1`
   - **Explanation:** Since there's only one element, it's the only equilibrium point.

3. **Input:** `arr[] = [1, 2, 3]`
   - **Output:** `-1`
   - **Explanation:** There is no equilibrium point in the given array.

## Constraints

- \(1 \leq \text{arr.size} \leq 10^6\)
- \(0 \leq \text{arr}[i] \leq 10^9\)

## Expected Time Complexity

- \(O(n)\)

## Expected Auxiliary Space

- \(O(1)\)