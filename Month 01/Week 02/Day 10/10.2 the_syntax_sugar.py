
def wrapper(func):
    def wrapped(*args,**kargs):
        print("code before the functions runs")
        result=func(*args,**kargs)
        print("code after the functions runs")
        return result
    return wrapped

@wrapper
def old_func():
    print("Main function is running")


old_func()