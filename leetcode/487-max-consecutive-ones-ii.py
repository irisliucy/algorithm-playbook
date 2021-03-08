# Author: irisliu (Iris Liu)
# Problem: (leetcode) 487-max-consecutive-ones-ii
# Title: Max Consecutive Ones II
# Link: https://leetcode.com/problems/max-consecutive-ones-ii/
# Idea: For a naive approach, we can use a nested for-loop to find all the possible sequences, update the number of zeros, calculate the max sequence. However, it takes O(n) time which is inefficient. An optimal approach will use a sliding window with 2 pointers. We move the window based on the validity of the sequence: < 1 0's in current window. If sequence is valid, we continue expanding it. Else, we contract the window until it's valid. We update the max sequence we've seen.
# Complexity. The optimal approach takes O(n) since both pointers only move forward. It takes O(1) space because we don't store other variable.
# Difficulty: Medium
# Tags: Arrays, Sliding window

class Solution:  
    def findMaxConsecutiveOnes(nums):
        max_ = 0
        i, j = 0, 0 # pointers
        zeros = 0

        whlie j < len(nums):  # while our window is in bound
            if nums[j] == 0:  # add rightmost element to window
                zeros += 1

            while zeros == 2:
                if nums[i] == 0:
                    zeros -= 1  # update zero count
                i += 1  # move the left pointer to contract the window

            max_ = max(max_, j - i + 1)
            j += 1  # expand the window

        return max_
