# Author: irisliu (Iris Liu)
# Problem: (leetcode) 283-move-zeros
# Title: Move Zeros
# Link: https://leetcode.com/problems/move-zeroes
# Idea: A simple in-place solution is to 1) bring all non-zero element to the front in one pass and 2) put 0 to the remaining array using a second pass. This solution takes 2for-loops and is sub-optimal even though the time complexity is O(n) i.e. [0,0,0,0,1]. An optimal solution is to do swaping during the pass. We need to add an additional pointer to keep track of the last non-zero index. In the for-loop, we swap the non-zero element at current index to the last non-zero index and increment the non-zero index pointer. 
# Complexity: It takes O(n) where n is the number of element in the array. It takes O(1) memory since the swapping and assignment is in-place.
# Difficulty: Easy
# Tags: Arrays, In-place

class Solution:    
    def moveZeros(nums):
        j = 0  # last non-zero element index
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


