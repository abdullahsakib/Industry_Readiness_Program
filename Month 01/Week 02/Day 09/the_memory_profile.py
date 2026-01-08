import sys

list=[i for i in range(1000000)]

generator=(i for i in range(1000000))

print(sys.getsizeof(list))

print(sys.getsizeof(generator))

# list comprehesion stores values and generator does not store values
