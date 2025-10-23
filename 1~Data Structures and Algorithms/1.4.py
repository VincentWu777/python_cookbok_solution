"""
Problem:
U want to make a list of the largest or smallest N items in a collection
"""
#Using heapd which has nlargest() and n smallest()

import heapq

nums = [1, 2, 8, 10, -1, 222, 0, 7]
print(heapq.nlargest(3, nums)) #[222, 10, 8]
print(heapq.nsmallest(3, nums)) #[-1, 0, 1]