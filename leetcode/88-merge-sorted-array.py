# Author: irisliu (Iris Liu)
# Problem: (leetcode) 88-merge-sorted-array
# Title: Merged Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/
# Idea: Simple solutions include merging two array and use a built-in sorted fn, but it will end up with O(m+n)log(m+n). To improve this, we can use a three pointer approach in one pass. Starting from the last element in the nums1 array, we iteratively compare the elements of nums2 and nums1 array and in-place write the element from the largest to the smallest. We have to handle the edge case when point 2, p2 < 0; the rest of elements in p1 will not be touched.
# Difficulty: Easy
# Tags: Arrays

class Solution:
    def merge(nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        for i in range(m+n-1, -1, -1):
            # edge case when p2 elements are all scanned
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums2[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
