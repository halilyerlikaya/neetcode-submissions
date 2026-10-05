class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start , end  = 0 , len(nums) -1 
        ind  = start + (end - start) //2
        while 1 :
            if target == nums[ind]:
                return ind
            elif target > nums[ind]:
                start  = ind +1 
                ind  = start + (end -start ) // 2
            else:
                end  = ind -1 
                ind =  start + (end -start )//2
            if start > end :
                return -1
            