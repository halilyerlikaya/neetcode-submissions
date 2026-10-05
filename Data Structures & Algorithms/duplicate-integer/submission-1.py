class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = dict()
        for item in nums:
            if item not in mydict:
                mydict[item] = True
                continue
            else:
                return True
        return False