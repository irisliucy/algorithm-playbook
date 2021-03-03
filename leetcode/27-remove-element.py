# Author: irisliu (Iris Liu)
# Problem: (leetcode) 27-remove-element
# Title: Remove Element
# Link: https://leetcode.com/problems/remove-element/
# Idea: We can simply start with a two pointer approach. Looping over the array, as we find the element is not equal to the value, we assign it to the current array index until the end. It takes O(n) time and O(1) space since the operation requires only 1 pass over the array and it's in-place. Another appraoch is to reduce the array size as we scan the val in the array and move them to the last. The worst case time will be still O(n) time and O(1) space but it will be more efficient if the elements to be remove is rare.
# Difficulty: Easy 
# Tags: Arrays

class Solution:
    def removeElement(nums, val):
        i = 0
        n = len(nums)
        while (i < n):
            if nums[i] == val:
                # move element to the last
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1

        return i
