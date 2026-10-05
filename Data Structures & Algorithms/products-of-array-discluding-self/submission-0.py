class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [x for x in nums]
        for i in range(1,len(nums)):
            nums[i] *= nums[i-1]
        for i in reversed(range(1,len(nums))):
            res[i-1] *= res[i]
        res[0] = res[1]
        for i in range(1,len(nums)-1):
            res[i] = nums[i-1] * res[i+1]
        res[-1] = nums[-2]
        return res