# Author: irisliu (Iris Liu)
# Problem: (leetcode) 941-valid-mountain-array
# Title: Valid Mountain Array
# Link: https://leetcode.com/problems/valid-mountain-array/
# Idea: Scan the array from left to right until we can't - that has to be a peak! We scan by detecting stringly up and then strictly down. If we reach the end, the array returns valid, else invalid. The scan will be bounded by O(n) where n is the number of elements in the array. Space complexity will be O(1). 
# Difficulty: Easy
# Tags: Arrays

class Solution:    
    def validMountainArray(arr):
        n = len(arr)
        i = 0

        # walk up
        while i < n - 1 and arr[i] < arr[i+1]:
            i+=1

        # peak cannot be  the first or last element
        if i == 0 or i == n-1:
            return False

        # walk down
        while i < n - 1 and arr[i] > arr[i+1]:
            i += 1

        return i == n - 1
