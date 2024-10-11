class Solution:    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        leaders_list = []
        
        # Initialize the maximum element from the right as the last element
        max_from_right = arr[-1]
        
        # The rightmost element is always a leader
        leaders_list.append(max_from_right)
        
        # Traverse the array from right to left
        for i in range(n-2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders_list.append(max_from_right)
        
        # Since we traversed from right to left, reverse the list before returning
        return leaders_list[::-1]