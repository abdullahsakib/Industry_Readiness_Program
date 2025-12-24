

import time

N=500000

nums=list(range(N))

start=time.time()
for i in range(N):
    nums.pop()

end=time.time()
time_taken=end-start

print(f"time taken by pop from end {time_taken}")


nums=list(range(N))
start=time.time()
for i in range(N):
    nums.pop(0)
end=time.time()
time_taken=end-start

print(f"time taken by pop from start {time_taken}")

