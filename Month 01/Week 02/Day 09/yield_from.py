def even():
    for i in range(10):
        if i%2==0:
            yield i
        

def odd():
    for i in range(10):
        if i%2 !=0:
            yield i



def combined():
    yield from even()
    yield from odd()


for i in combined():
    print(i)