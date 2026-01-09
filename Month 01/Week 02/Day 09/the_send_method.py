
def  accumulator():
    sum=0
    while True:
        value = yield sum
        if value is None:
            continue
        sum+=value



gen= accumulator()

print(gen.send(None))

print(gen.send(2))
print(gen.send(2))
print(gen.send(None))
print(gen.send(2))

