


import time

data=list(range(1000000))
start =time.time()

length=len(data)

print(length)
    
end=time.time()
time_taken=end-start

print(f"time taken by len {time_taken}")


