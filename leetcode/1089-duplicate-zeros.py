# Author: irisliu (Iris Liu)
# Problem: (leetcode) 1089-dupulicate-zeros
# Title: Duplicate Zeros
# Link: https://leetcode.com/problems/duplicate-zeros/
# Idea: The key is to find how many zeros to duplicate and the boundary of the array to be copied. One solution is to do a two pass, time is bounded by O(n). We can improve it with just one pass and copy elements backwards and handle the edge case when a duplicated zero is out of boundary.
# Difficulty: easy 
# Tags: arrays
from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)

        for i in range(n-1, -1, -1):
            # copy valid element
            if i + zeroes < n:
                arr[i+zeroes] = arr[i]
            # copy twice if element == 0
            if  arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i+zeroes] = 0
