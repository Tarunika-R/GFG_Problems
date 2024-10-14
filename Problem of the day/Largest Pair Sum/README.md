# Largest Pair Sum

## Problem Description

Find the largest pair sum in an array of distinct integers.

## Examples

### Example 1
- **Input**: `arr[] = [12, 34, 10, 6, 40]`
- **Output**: `74`
- **Explanation**: Sum of 34 and 40 is the largest, i.e., 34 + 40 = 74.

### Example 2
- **Input**: `arr[] = [10, 20, 30]`
- **Output**: `50`
- **Explanation**: Sum of 20 and 30 is the largest, i.e., 20 + 30 = 50.

## Constraints
- `2 ≤ arr.size() ≤ 10^6`
- `0 ≤ arr[i] ≤ 10^6`

## Expected Time Complexity
- O(n)

## Expected Auxiliary Space
- O(1)

## Approach

To find the largest pair sum in an array of distinct integers, we need to identify the two largest numbers in the array and sum them. This can be achieved in a single pass through the array, ensuring the solution is efficient with a time complexity of O(n) and constant space complexity O(1).

### Algorithm
1. Initialize two variables `first_max` and `second_max` to negative infinity. This ensures that any number in the array will be larger than these initial values.
2. Iterate through each number in the array:
   - If the current number is greater than `first_max`, update `second_max` to be `first_max` and then set `first_max` to the current number.
   - Otherwise, if the current number is greater than `second_max`, update `second_max` to the current number.
3. Return the sum of `first_max` and `second_max`.

