def maximum_time(time):

    # use 'replace' to replace character and assign back to the value
    # handle hours
    if time[0] == '?':
        time = time.replace(time[0], '2', 1) if (time[1] <= '3' or time[1] == '?') else time.replace(time[0], '1', 1)

    if time[1] == '?':
        time = time.replace(time[1], '3', 1) if (time[0] == '2') else time.replace(time[1], '9', 1)

    # handle minutes
    if time[3] == '?':
        time = time.replace(time[3], '5', 1)

    if time[4] == '?':
        time = time.replace(time[4], '9', 1)
        
    return time

######
# Time Complexity = O(1)  
# Space Complexity = O(1)       replace digit(s) in-place
######

def maximum_time1(s):
    # convert string to list for item assignment
    s = list(s)
    
    if s[0] == '?':
        s[0] = '2' if s[1] <= '3' or s[1] == '?' else '1'
    if s[1] == '?': s[1] = '9' if s[0] != '2' else '3'
    if s[3] == '?': s[3] = '5'
    if s[4] == '?': s[4] = '9'
    
    # convert list to string
    return ''.join(s)

######
# Time Complexity = O(1)  
# Space Complexity = O(1)       replace digit(s) in-place
######

######
#Test#
######
import time
start_time = time.time()

input = "23:5?"
assert maximum_time1(input) == "23:59"

input = "2?:22"
assert maximum_time1(input) == "23:22"

input = "0?:??"
assert maximum_time1(input) == "09:59"

input = "1?:??"
assert maximum_time1(input) == "19:59"

input = "?4:??"
assert maximum_time1(input) == "14:59"

input = "?3:??"
assert maximum_time1(input) == "23:59"

input = "??:??"
assert maximum_time1(input) == "23:59"



print("Yay! All test cases pass in {}ms".format(time.time()-start_time))