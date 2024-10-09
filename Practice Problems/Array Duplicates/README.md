# Find Duplicates in an Array

## Problem Description

Given an array `arr` of size `n` which contains elements in the range from `0` to `n-1`, you need to find all the elements occurring more than once in the given array. The answer should be returned in ascending order. If no such element is found, return a list containing `[-1]`.

## Examples

### Example 1
- **Input**: `n = 4, arr = [0, 3, 1, 2]`
- **Output**: `[-1]`
- **Explanation**: There is no repeating element in the array. Therefore, the output is `[-1]`.

### Example 2
- **Input**: `n = 5, arr = [2, 3, 1, 2, 3]`
- **Output**: `[2, 3]`
- **Explanation**: Elements `2` and `3` occur more than once in the given array.

## Constraints
- `1 <= n <= 10^5`
- `0 <= arr[i] <= 10^5` for each valid `i`

## Solution

The solution involves using a dictionary to count the occurrences of each element in the array and then collecting the elements that occur more than once.

### Expected Time Complexity
- O(n)

### Expected Auxiliary Space
- O(n)

## Approach

To solve this problem efficiently, we will use a dictionary to count the occurrences of each element in the array. Then, we will identify the elements that occur more than once and return them in ascending order.

### Algorithm
1. Initialize an empty dictionary `count` to keep track of the frequency of each element.
2. Initialize an empty list `result` to store the elements that occur more than once.
3. Iterate through each element `num` in the array `arr`:
   - If `num` is already a key in the dictionary `count`, increment its value by 1.
   - If `num` is not in the dictionary, add it as a key with the value 1.
4. Iterate through the items (key-value pairs) in the dictionary `count`:
   - For each element `num` and its frequency `freq`, if `freq` is greater than 1, add `num` to the `result` list.
5. If the `result` list is empty (i.e., no elements occurred more than once), return `[-1]`.
6. Return the `result` list sorted in ascending order.