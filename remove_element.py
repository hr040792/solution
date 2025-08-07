def removeElement(nums, val):
    i = 0  # pointer for the position to overwrite
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
