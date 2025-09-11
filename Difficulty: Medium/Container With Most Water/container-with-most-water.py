class Solution:
    def maxWater(self, arr):
        max_area = 0
        left = 0 
        right = len(arr) - 1
        
        while left < right:
            max_area = max(max_area, (right - left) * min(arr[left], arr[right]))
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return max_area
        