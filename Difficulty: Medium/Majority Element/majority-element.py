from collections import Counter

class Solution:
    def majorityElement(self, arr):
        count = Counter(arr)
        n = len(arr)
        for key, value in count.items():
            if value > n // 2:
                return key
        return -1