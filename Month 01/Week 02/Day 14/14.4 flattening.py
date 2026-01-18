

def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            yield from (flatten(i))

        else:
            yield i

data = [1, [2, [3, 4]]]
print(list(flatten(data)))