
def contains(list, target):
    data_set =set(list)
    if target in data_set:
        return True
    else:
        return False
    
    

print(contains(range(1000000), -5))