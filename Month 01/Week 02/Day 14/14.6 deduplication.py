

def remove_duplication(lst):
    seen=set()
    result=[]

    for i in lst:
        if i not in seen:
            seen.add(i)
            result.append(i)
    
    return result



print(remove_duplication([1,2,3,4,5,5,6,6,6,7,7,8,9,9]))


    