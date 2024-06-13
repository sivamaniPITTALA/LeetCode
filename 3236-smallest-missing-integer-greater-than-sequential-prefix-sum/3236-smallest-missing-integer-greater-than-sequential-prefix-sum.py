class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        s = nums[0]
        idx = 1
        while idx<len(nums) and nums[idx] == nums[idx-1]+1:
            s+=nums[idx]
            idx+=1
        while s in num_set:
            s+=1
        
        return s