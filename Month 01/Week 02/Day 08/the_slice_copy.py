

import time


list=list(range(10000000))
start =time.time()

slice=list[100:900000]
    
end=time.time()
time_taken=end-start

print(f"time taken {time_taken}")