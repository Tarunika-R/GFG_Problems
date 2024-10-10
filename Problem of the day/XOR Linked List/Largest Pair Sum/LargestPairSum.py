from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        
        first_max = second_max = float('-inf')  # Initialize the two largest numbers

        # Iterate through the array to find the two largest numbers
        for num in arr:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num

        # Return the sum of the two largest numbers
        return first_max + second_max