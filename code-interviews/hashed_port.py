from collections import deque
def hashedPorts(n, T, packet_id):
    ans, t = [], 1
    avail = [0] * n
    queue = deque()
    for pid in packet_id:
        print(avail)
        # pop from queue if the port is available
        while queue and avail[queue[0]] <= t:
            queue.popleft()
        # if no ports available, wait until there is one available
        if len(queue) == n:
            t = avail[queue.popleft()]
        # try port until find one available
        port = pid % n
        while avail[port] > t:
            port = (port + 1) % n
        # send packet, update available time for the port
        avail[port] = t + T
        queue.append(port)
        ans.append(port)
        t += 1
    return ans

n = 5
T = 10
packid = [1, 2, 3, 4, 5, 6]
print(hashedPorts(n, T, packid)) # [1, 2, 3, 4, 0, 1]