# Author: irisliu (Iris Liu)
# Problem: (leetcode) 414-third-maximum-number
# Title: Third Maximum Number
# Link: https://leetcode.com/problems/third-maximum-number/
# Idea: The key is to use set() to keep distinct elements of the seen maximum values so far. The seen maximum will contain 3 elements at most. As we scan through the array, we add a new element to the set, if it exceeds 3 elements, we remove the smallest element until the end. After that, we return the min element of the set if the set contains exactly 3 elements. Else, we return the max of the set. 
# Complexity: Inserting and removing element from set will take O(1) each. Hence, the for-loop will takes O(n) since it performs this operation for each element. Finding and returning the min or max value from set is also O(1). Therefore, the total time complexity is O(n). The space complexity will be O(1) since the set will never holds more than 3 elements.
# Difficulty: Easy
# Tags: Arrays, Set

class Solution:    
    def thirdMax(nums):
        seen_max = set()

        for i in range(nums):
            seen_max.add(i)
            if len(seen_max) > 3:
                seen_max.remove(min(seen_max)) # remove min element if there are > 3 elements in set

        if len(seen_max) == 3:
            return min(seen_max)  # return third maximum

        return max(seen_max)  # return max
