# Author: irisliu (Iris Liu)
# Problem: (leetcode) 1299-replace-elements-with-greatest-element-on-right-side
# Title: Replace Elements with Greatest Element on Right Side
# Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Idea: The key idea is to scan the array backwards. We start by setting the last elment to -1 and use max_ to keep track of the max values from the right. Then, we scan from the second last element all the way to the first element, update max_ and replace element with max values along the way.
# Complexity: The method is in-place, it takes only O(1) memory. And it scans the elements in the array in one pass, it takes O(n) time.
# Difficulty: Easy
# Tags: Arrays

class Solution:
    def replaceElements(arr):
        max_, arr[-1] = arr[-1], -1

        for i in range(len(arr) -2, -1, -1):
            max_, arr[i] = max(max_, arr[i]), max_

        return arr
