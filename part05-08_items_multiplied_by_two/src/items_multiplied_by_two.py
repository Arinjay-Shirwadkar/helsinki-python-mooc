def double_items(nums: list):
    copy = nums[:]
    for i in range(0,len(copy)):
        copy[i]*=2
    return copy
