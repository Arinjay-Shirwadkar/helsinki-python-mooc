def remove_smallest(nums: list):
    min = nums[0]
    for i in nums:
        if i<min:
            min =i
    nums.remove(min)