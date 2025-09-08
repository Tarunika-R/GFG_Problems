#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        count = 0
        nums = [int(digit) for digit in str(n)]
        for i in nums:
            if i != 0:
                if n % i == 0:
                    count += 1
        return count