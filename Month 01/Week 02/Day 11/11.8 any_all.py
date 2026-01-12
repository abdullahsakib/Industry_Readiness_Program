
number=[-1,-2,-3,4,5,-6,-9]

negative=any(n<0 for n in number)

print("is any number negative", negative)

all_positive=all(n>0 for n in number)
print("are all number positive", all_positive)


