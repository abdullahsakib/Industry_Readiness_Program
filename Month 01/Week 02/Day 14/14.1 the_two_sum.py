

def two_sum(nums, target):
    seen=set()

    for num in nums:
        need =target-num
        if need in seen:
            return num, need
        seen.add(num)
    
    return None



print(two_sum([1,2,3,4,5,6,7,9,],9))
