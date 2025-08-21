from collections import Counter

class Solution:
    def countFreq(self, arr, target):
        freq = Counter(arr)
        return freq[target]
        