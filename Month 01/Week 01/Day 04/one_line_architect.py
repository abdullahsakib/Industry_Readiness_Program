
nums=[]

for i in range(1,11):
    nums.append(i)
    
square= [x**2 for x in nums if x%2==0]

print(square)
    