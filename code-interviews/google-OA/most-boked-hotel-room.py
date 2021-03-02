import collections
import time

def mostBookedHotelRoom(bookings):
    bookkeeping = collections.defaultdict(lambda: [0, 0]) # tuple (a, b): a represents the numbering of booking, b represent if it's free

    for booking in bookings:
        room = booking[1:]  # stripe the symbol
        status = booking[0]

        # if the room is requested to be booked and it's freed
        if status == '+' and bookkeeping[room][1] >= 0:
            bookkeeping[room][0] += 1
            bookkeeping[room][1] = -1

        if status == '-':
            bookkeeping[room][1] = 0



    # mostbookroom = sorted(bookkeeping.items(), key=lambda x: (-x[1][0], x[0]))
    return sorted(bookkeeping.items(), key=lambda x: (-x[1][0], x[0]))[0][0]

######
# Time Complexity = O(n log n)  bounded by sorted function (timsort)
# Space Complexity = O(1)       bounded by the size of bookkeeping dict
######

def mostBookedHotelRoom1(bookings):
    bookkeeping = collections.defaultdict(lambda: [0, 0]) # tuple (a, b): a represents the numbering of booking, b represent if it's free

    for booking in bookings:
        room = booking[1:]  # stripe the symbol
        status = booking[0]

        # if the room is requested to be booked and it's freed
        if status == '+' and bookkeeping[room][1] >= 0:
            bookkeeping[room][0] += 1
            bookkeeping[room][1] = -1

        if status == '-':
            bookkeeping[room][1] = 0

    freq = 0
    mostbookroom = bookings[0]  # by default, the first room
    for k, v in bookkeeping.items():
        if v[0] > freq:
            freq = v[0]
            mostbookroom = k
        elif v[0] == freq:
            if str(k[0]) < str(mostbookroom[0]):
                mostbookroom = k
    return mostbookroom

######
# Time Complexity = O(n)        bounded by for-loop of dict size=n
# Space Complexity = O(1)       bounded by the size of bookkeeping dict
######


######
#Test#
######
start_time = time.time()
input = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
assert mostBookedHotelRoom(input) == "1A"

input = ["+3A", "+3E", "+3A", "+4F", "+3A", "-3E"]
assert mostBookedHotelRoom(input) == "3A"

input = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+3E", "+3E", "-3E", "-3E"]
assert mostBookedHotelRoom(input) == "1A"

input = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+3E", "-3E", "+3E", "-3E"]
assert mostBookedHotelRoom(input) == "3E"

print("Yay! All test cases pass in {}ms".format(time.time()-start_time))

        
