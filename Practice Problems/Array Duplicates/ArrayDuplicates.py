from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        
        count = {}
        result = []
        
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num, freq in count.items():
            if freq > 1:
                result.append(num)
        
        if not result:
            return [-1]
        
        return sorted(result)