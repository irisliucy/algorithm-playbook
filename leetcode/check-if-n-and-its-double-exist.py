# Author: irisliu (Iris Liu)
# Problem: (leetcode) 1346-check-if-n-and-its-double-exist
# Title: Check If N and Its Double Exist
# Link: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
# Idea: Lookup in array is O(n), which is expensive. If we can reduce the lookup time, we can reduce the overall time complexity of the solution. One way is to convert the array to set and do the lookup for (i*2 in set), the operation takes O(1) time.
# Difficulty: Easy
# Tags: Arrays

class Solution:
    def checkIfExist(arr):
        if arr.count(0) > 1: return True
        s = set(arr) - {0} # convert array to set and remove all 0
        for i in arr:
            if i*2 in s:
                return True
        return False
