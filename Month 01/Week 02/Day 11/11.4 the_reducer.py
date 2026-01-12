from functools import reduce

list=[1,2,3,4,5,6]

product=reduce(lambda x,y : x*y, list)

print(product)