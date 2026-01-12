

def wrapper(func):
    def wrapped():
        print("code before the functions runs")
        result=func()
        print("code after the functions runs")
        return result
    return wrapped

@wrapper
def old_func(name):
    print(f"Your name is {name}")


old_func("Sakib")

# Wrapper that takes no argument is valid for function that accepts no argument