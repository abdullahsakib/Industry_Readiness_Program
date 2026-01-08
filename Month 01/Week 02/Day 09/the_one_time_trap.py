

def gen():
    yield 1
    yield 2
    yield 3

g=gen()

for i in g:
    print(i)


# 2ND TIME

for i in g:
    print(i)


# Once Run Generator is exhausted

