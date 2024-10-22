class Solution:
    def getSecondLargest(self, arr):
        first_largest = second_largest = -1

        for num in arr:
            if num > first_largest:
                second_largest = first_largest
                first_largest = num
            elif num > second_largest and num < first_largest:
                second_largest = num

        return second_largest