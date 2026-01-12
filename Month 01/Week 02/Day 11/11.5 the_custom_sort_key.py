
values = ["100px", "20px", "3px"]

print(sorted(values, key=lambda x: int(x[:-2])))