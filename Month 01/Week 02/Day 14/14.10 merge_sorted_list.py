
def merge(a,b):
    i,j=0,0
    merged=[]

    while i < len(a) and j < len(b):

        if a[i]< b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])

            j+=1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged


a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

print(merge(a,b))
        
