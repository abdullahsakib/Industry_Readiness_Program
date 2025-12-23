
import time

nums=[]

start=time.time()
for i in range(200000):
    nums.append(i)

end=time.time()
time_taken=end-start

print(f"time taken by append {time_taken}")


nims=[]
start=time.time()
for i in range(200000):
    nums.insert(0,i)
end=time.time()
time_taken=end-start

print(f"time taken by insert {time_taken}")


