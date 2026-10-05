class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longg = 0 
        for num in mySet:
            if (num-1) not  in mySet:
                length = 1 
                while (num+length) in mySet:
                    length +=1
                longg = max(length,longg)
        return longg
