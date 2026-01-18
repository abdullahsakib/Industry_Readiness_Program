
def find_missing(nums):
    expected_sum=100*101//2
    actual_sum=sum(nums)

    return expected_sum-actual_sum


nums=list(range(1,101))
nums.remove(33)

print(find_missing(nums))