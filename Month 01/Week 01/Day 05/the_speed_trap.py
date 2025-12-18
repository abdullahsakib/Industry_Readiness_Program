import time

nums = list(range(1000000))
nums_set = set(nums)

start= time.perf_counter()
-1 in nums
end=time.perf_counter()

print("time needed for list lookup", end-start)   


start= time.perf_counter()
-1 in nums_set
end=time.perf_counter()

print("time needed for set lookup", end-start)   


