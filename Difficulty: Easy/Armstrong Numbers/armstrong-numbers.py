#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        string = str(n)
        p_sum = 0
        for i in string:
            p_sum += int(i) ** 3
        return p_sum == n