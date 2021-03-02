def min_abs_difference_of_server_loads(processes):
    # knapsack 1/0 problem
    # 1. maximize the load of server 
    # 2. bound the load to (totalProcessesload/2)

    # recurrence formula
    # either take it or not
    # if take it, the capacity will reduces and the loads will increase
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-processes[i-1]] + processes[i-1]) when processes[i-1] <= j else dp[i-1][j]

    # bound of the maximum load per machine
    s = sum(processes) // 2
    n = len(processes)
    
    # 1. initial the table (memoization)
    dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1): # num of process
        for j in range(1, s + 1): # capacity
            # 2. recurrence formula
            if processes[i - 1] <= j:
                # optimal solution
                # add the process to the server if the process is smaller than max load per machine
                dp[i][j] = max(dp[i - 1][j], processes[i - 1] + dp[i - 1][j - processes[i - 1]])
            else:
                # not add the process
                dp[i][j] = dp[i - 1][j]
    '''return second server loads - first server loads'''
    return (sum(processes) - dp[-1][-1]) - dp[-1][-1]
    

######
# Runtime: O(sn) where s is the sum of all processes and n is the number of processes
# space: O(sn)
######

######
#Test#
######
import time
start_time = time.time()
input = [1, 2, 3, 4, 5]
print(min_abs_difference_of_server_loads(input))
assert min_abs_difference_of_server_loads(input) == 1

input = [10, 10, 9, 9, 2]
assert min_abs_difference_of_server_loads(input) == 0

input = []
assert min_abs_difference_of_server_loads(input) == 0

input = [1]
assert min_abs_difference_of_server_loads(input) == 1

print('Awesome, you pass all test cases in {}'.format(time.time() - start_time))