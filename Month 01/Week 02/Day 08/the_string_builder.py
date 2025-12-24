
import time


s=""
start =time.time()
for i in range(10000):
    s += "a"
    
end=time.time()
time_taken=end-start

print(f"time taken by string {time_taken}")


s=""
start =time.time()

char=[]
for i in range(10000):
    char.append("a")

s="".join(char)
    
end=time.time()
time_taken=end-start

print(f"time taken by join {time_taken}")
