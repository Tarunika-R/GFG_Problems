class Solution:
    def checkSorted(self, arr):
        # Create a sorted version of the array
        sorted_arr = sorted(arr)
        
        # Identify mismatches
        mismatches = [i for i in range(len(arr)) if arr[i] != sorted_arr[i]]
        
        # Check the number of mismatches
        if len(mismatches) == 0:
            return True  # Already sorted
        elif len(mismatches) == 2:
            return False  # Only one swap needed, not valid for exactly two swaps
        elif len(mismatches) == 4:
            # Extract mismatched indices
            i1, i2, i3, i4 = mismatches
            
            # Check if we can swap the elements at these indices to sort the array
            # Swap pairs: (i1, i3) and (i2, i4) or (i1, i4) and (i2, i3)
            return (arr[i1] == sorted_arr[i3] and arr[i3] == sorted_arr[i1] and
                    arr[i2] == sorted_arr[i4] and arr[i4] == sorted_arr[i2]) or \
                   (arr[i1] == sorted_arr[i4] and arr[i4] == sorted_arr[i1] and
                    arr[i2] == sorted_arr[i3] and arr[i3] == sorted_arr[i2])
        
        return False