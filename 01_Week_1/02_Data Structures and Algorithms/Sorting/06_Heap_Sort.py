import heapq

arr = [12, 11, 13, 5, 6, 7]

heapq.heapify(arr)

sorted_arr = []

while arr:
    sorted_arr.append(heapq.heappop(arr))

print("Heap Sort:", sorted_arr)