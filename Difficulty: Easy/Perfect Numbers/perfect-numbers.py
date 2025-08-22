import math

class Solution:
    def isPerfect(self, n):
        sum_ = 1
        sqrt = int(math.sqrt(n))
        for i in range(2, sqrt + 1):
            if n % i == 0:
                sum_ += i
                if i != n // i:
                    sum_ += n // i
        return n == sum_        
        
                