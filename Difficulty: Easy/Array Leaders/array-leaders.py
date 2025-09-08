class Solution:
    def leaders(self, arr):
        got = []
        n = len(arr)
        # for i in range(0, n):
        #     leader = True
        #     for j in range(i + 1, n):
        #         if arr[i] < arr[j]:
        #             leader = False
        #             break
        #     if leader:
        #         got.append(arr[i])
        # return got
        
        max_from_right = arr[-1]
        got.append(max_from_right)
        
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                got.append(arr[i])
        return (got[::-1])
        
                    