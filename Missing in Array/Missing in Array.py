def find_missing_element(arr):
    n = len(arr) + 1  # Calculate n
    total_sum = n * (n + 1) // 2  # Calculate the expected sum
    arr_sum = sum(arr)  # Calculate the actual sum
    return total_sum - arr_sum  # The missing element

# Example usage
arr1 = [1, 2, 3, 5]
print("The missing element is:", find_missing_element(arr1))  # Output: 4

arr2 = [1]
print("The missing element is:", find_missing_element(arr2))  # Output: 2