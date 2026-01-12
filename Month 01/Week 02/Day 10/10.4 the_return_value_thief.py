
def wrapper(func):
    def wrapped(*args,**kargs):
        print("code before the functions runs")
        func(*args,**kargs)
        print("code after the functions runs")
    return wrapped

@wrapper
def old_func(name):
    print(f"Your name is {name}")


res=old_func("Sakib")
print(res)

# as fun forgot to return func(*args) return is none