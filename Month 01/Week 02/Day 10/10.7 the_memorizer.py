
def cache(func):
    store={}

    def wrapper(*args):
        if args in store:
            return store[args]
        print("computing")
        result= func(*args)
        store[args]=result

        return result
    return wrapper

@cache
def add(a,b):
    print("running slow")
    return a+b

print(add(4,5))
print(add(10,5))
print(add(4,5))