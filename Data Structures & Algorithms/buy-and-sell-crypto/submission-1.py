class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res =  0
        loww  =prices[0]
        for price in prices:
            if price < loww:
                loww  = price
            res = max( res, price - loww)
        return res