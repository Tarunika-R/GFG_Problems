class Solution:
    def equilibriumPoint(self, arr):
        n = len(arr)
        
        total_sum = sum(arr)
        
        left_sum = 0
        
        for i in range(n):
            total_sum -= arr[i]
            
            if left_sum == total_sum:
                return i + 1  
            
            left_sum += arr[i]
        
        return -1