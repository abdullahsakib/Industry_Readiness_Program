def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
    
fib=fibonacci()

for i in range(4):
    print(next(fib))