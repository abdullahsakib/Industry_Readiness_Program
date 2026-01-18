

def find_item(target,nums):
    left=0
    right=len(nums)-1
    while left<=right:
        mid = (left + right) // 2   

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1          
        else:
            right = mid - 1 
    return -1

print(find_item(8,[1,2,3,5,6,7,8,9,10,11,12,13,15,16]))