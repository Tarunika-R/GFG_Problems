class Solution:
    def maxDistance(self, arr):
        # Dictionary to store the first occurrence of each element
        first_occurrence = {}
        max_dist = 0

        # Traverse the array
        for i in range(len(arr)):
            if arr[i] in first_occurrence:
                # Calculate the distance from the first occurrence
                dist = i - first_occurrence[arr[i]]
                # Update the maximum distance if necessary
                max_dist = max(max_dist, dist)
            else:
                # Store the index of the first occurrence
                first_occurrence[arr[i]] = i

        return max_dist