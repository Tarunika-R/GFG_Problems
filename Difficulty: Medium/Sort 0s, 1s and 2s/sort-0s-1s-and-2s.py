class Solution:
    def sort012(self, arr):
        # for i in range(0, len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         if arr[i] > arr[j]:
        #             arr[i], arr[j] = arr[j], arr[i]
        # return arr
        
        count0 = count1 = count2 = 0
        
        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            elif num == 2:
                count2 += 1
        
        i = 0
        while count0 > 0:
            arr[i] = 0
            i += 1
            count0 -= 1
        
        while count1 > 0:
            arr[i] = 1
            i += 1
            count1 -= 1
        
        while count2 > 0:
            arr[i] = 2
            i += 1
            count2 -= 1
        return arr
            
        