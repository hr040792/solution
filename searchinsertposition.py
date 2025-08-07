def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    # Binary Search
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    # If not found, left is the correct insertion position
    return left
