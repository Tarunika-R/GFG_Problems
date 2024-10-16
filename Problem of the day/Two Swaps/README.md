# Two Swaps Sorting Problem

## Problem Statement

Given a permutation of some of the first natural numbers in an array `arr[]`, determine if the array can be sorted in exactly two swaps. A swap can involve the same pair of indices twice.

### Return
Return `true` if it is possible to sort the array with exactly two swaps, otherwise return `false`.

### Examples

#### Example 1
- **Input:** `arr = [4, 3, 2, 1]`
- **Output:** `true`
- **Explanation:** First, swap arr[0] and arr[3]. The array becomes [1, 3, 2, 4]. Then, swap arr[1] and arr[2]. The array becomes [1, 2, 3, 4], which is sorted.


#### Example 2
- **Input:** `arr = [4, 3, 1, 2]`
- **Output:** `false`
- **Explanation:** It is not possible to sort the array with exactly two swaps.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^6`
- `1 ≤ arr[i] ≤ arr.size()`

## Solution Outline

1. **Identify Mismatches:** Compare the given array with a sorted version of the same array to find mismatched positions.
2. **Check Number of Mismatches:**
   - If there are `0` mismatches, the array is already sorted.
   - If there are exactly `2` mismatches, it means one swap is needed, which is not allowed.
   - If there are exactly `4` mismatches, verify if two swaps can sort the array.
   - For any other number of mismatches, sorting with exactly two swaps is not possible.
3. **Return Result:** Based on the analysis of mismatched positions, return `true` or `false`.






