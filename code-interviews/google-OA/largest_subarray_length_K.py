# Input: array A contains N distinct integers, K
# Output: largest subarray

Class Solution:
	def largestSubarrayLength(a, k):
		# store the first starting index for subarray as largest
		first_index = 0

		# find the subarrays
		for i in range(len(a) - k + 1):
			# replace the largest first index if a larger value is detected
			if a[i] > a[first_index]:
				first_index = i

        return a[first_index:first_index+k]		

    # Time Complexity: O(n)
    # Space Complexity = O(1) 

    ## if A contains non distint elements
    def largest_subarray_indistinct(a, k):
        first_idx = 0
        for x in range(1, len(a) - k + 1):
            # compare values at each index for the would be sub arrays
            for i in range(k):
            # replace the largest index and break out of the inner loop is larger value is found
            if a[first_idx + i] < a[x + i]:
                first_idx = x
                break
            # if the current stored largest subarray is larger than the current subarray, move on
            elif a[first_idx + i] > a[x + i]:
                break

        return a[first_idx:first_idx+k]

    # Time Complexity: O(nk)
    # Space Complexity = O(1) 

# result = Solution()
# result.largestSubarrayLength(a, k)
