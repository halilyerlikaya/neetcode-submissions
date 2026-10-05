class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result  =[]
        nums = sorted(nums)
        for i , num in enumerate(nums):
            if i >= 1 and num == nums[i-1 ]: 
                continue
            j,k  = i + 1 , len(nums)-1
            while j < k :
                if nums[j] + nums[k] + nums[i] == 0 :
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1 
                    k -=1 
                    while nums[j] == nums[j-1 ] and j <k:
                        j+=1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                elif nums[j] + nums[k]  +  nums[i]< 0 :
                    j+= 1 
        return result

        