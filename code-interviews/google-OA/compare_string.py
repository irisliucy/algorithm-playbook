import collections, bisect
def compare_string(A, B):

    a = A.split(',')
    b = B.split(',')
    m = len(a)
    n = len(b)


    result = []
    for i in range(n):
        counter = 0
        for j in range(m):
            if collections.Counter(b[i]).most_common(1)[0][1] > collections.Counter(a[j]).most_common(1)[0][1]:
                counter += 1
        result.append(counter)

    return result

# Runtime: O(mn) where m is the size of array A and n is the size array B
# Space complexity: O(n)  C array grows with B array

def compare_string1(A, B):

    a_list = A.split(',')
    b_list = B.split(',')

    result = []
    for b in b_list:
        counter = 0
        for a in a_list:
            if b.count(min(b)) > a.count(min(a)):
                counter += 1
        result.append(counter)

    return result

# Runtime: O(mn) where m is the size of array A and n is the size array B
# Space complexity: O(n)  C array grows with B array

def compare_string2(queries, words):

    words_freq = sorted([word.count(min(word)) for word in words])  # Do a count of min word in the words array
    print(words_freq)
    result = []
    for query in queries:
        q_min=min(query) # Get the minimum letter 
        q_count=query.count(q_min) # Count frequency of letter
        result.append(len(words) - bisect.bisect(words_freq, q_count )) # Do a binary search and find the items that have more frequency of min char
    return result

######
#Test#
######
import time
start_time = time.time()

A = "abcd,aabc,bd"
B = "aaa,aa"
assert compare_string(A, B) == [3, 2]

A = ["bbb","cc"]
B = ["a","aa","aaa","aaaa"]
# print(compare_string2(A,B))
assert compare_string2(A,B) == [1,2]


print("Yay! All test cases pass in {}ms".format(time.time()-start_time))