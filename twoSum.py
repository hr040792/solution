def twoSum(self, nums : list [int], target : int) -> list[int]:
    numMap = {}
    for i, num in enumerate(nums):
        comp = target - num 
        if comp in numMap:
            return [numMap[comp], i]
        numMap[num] = i
        
        
        
        