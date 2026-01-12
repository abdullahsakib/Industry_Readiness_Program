
from functools import partial

def power(base,exp):
    return base**exp

squre =partial(power, exp=2)


print(squre(5))