# question: https://www.geeksforgeeks.org/repeatedly-search-element-doubling-every-successful-search/
def solution(a, b):
    sorted_arr = sorted(a)
    mx = sorted_arr[len(sorted_arr) - 1]

    def binary_search(arr, high, low, target):
        if high is None: 
            high = len(arr) 
        while low < high: 
            mid = (low + high)//2
            midval = arr[mid] 
            
            if midval < target: 
                low = mid + 1
            elif midval > target:  
                high = mid 
            else: 
                return mid 
        return -1
            
    while (b < mx):
        if (binary_search(sorted_arr, len(sorted_arr), 0, b) != -1):
            b *= 2
        else:
            return b
    return b

a = [1, 2, 3]
b = 1
assert (solution(a, b) == 4)

a = [1, 3, 5, 2, 12]
b = 3
assert (solution(a, b) == 6)
print('Pass all test cases!')

    