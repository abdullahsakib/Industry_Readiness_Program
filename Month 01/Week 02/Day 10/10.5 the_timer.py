
import time

def timeit(func):
    def wrapper(*args,**kargs):
        start=time.time()
        result=func(*args,**kargs)
        end=time.time()

        print(f"{func.__name__} took {end-start:.5f} seconds")
    return wrapper

numbers=list(range(1_000_000))

@timeit
def using_map():
    return list(map(lambda x:x*x, numbers))  

@timeit
def using_list_comprehension():
    return [x*x for x in numbers]  

using_map()
using_list_comprehension()
