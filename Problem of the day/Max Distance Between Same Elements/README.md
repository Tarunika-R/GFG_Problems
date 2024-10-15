# Max Distance Between Same Elements

## Difficulty
Easy

## Problem Statement
Given an array `arr[]` with repeated elements, the task is to find the maximum distance between two occurrences of an element.

You may assume that every input array has repetitions.

## Examples

### Example 1
- **Input**: `arr = [1, 1, 2, 2, 2, 1]`
- **Output**: `5`
- **Explanation**: Distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, so max distance is 5.

### Example 2
- **Input**: `arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]`
- **Output**: `10`
- **Explanation**: Maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2, maximum distance for 4 is 10-5 = 5, so max distance is 10.

---

## Constraints
- `1 <= arr.size() <= 10^6`
- `1 <= arr[i] <= 10^9`

## Expected Time Complexity
- `O(n)`

## Expected Auxiliary Space
- `O(n)`

## Solution

To solve this problem efficiently with \(O(n)\) time complexity and \(O(n)\) auxiliary space, we can use a dictionary to keep track of the first occurrence of each element. As we iterate through the array, we can update the maximum distance for each element.
