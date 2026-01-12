
def add():
    return lambda x,y:x+y

sum=add()

print(sum(4,5))