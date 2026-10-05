class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict =  {}
        freqs = [[] for i in range(len(nums)+1)]
        for num in nums:
            myDict[num] =  1 + myDict.get(num,0)
        for key,value in myDict.items():
            freqs[value].append(key)
        i = 0 
        result = []
        while i < k :
            i  += len(freqs[-1])
            result = result + freqs[-1]
            freqs.pop()
        return result
