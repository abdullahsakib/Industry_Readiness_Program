
import time

list_a=[2,4,5,6,7,8,11,22,10,2]

list_b=[11,23,45,55,66,77,88,9]

duplicates=[]

start =time.time()

for i in list_a:
    for j in list_b:
        if i==j:
            duplicates.append(i)

print(duplicates)
    
end=time.time()
time_taken=end-start

print(f"time taken  {time_taken}")