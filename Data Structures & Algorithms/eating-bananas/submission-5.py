class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end  = 1, max(piles)
        result = end
        while start <=  end:
            ind  = (start + end) // 2 
            totalTime  = 0
            for p in piles :
                totalTime  += math.ceil(float(p) / ind )
            if totalTime <= h: 
                result  = ind 
                end = ind-1 
            else: 
                start = ind + 1 
        return result
