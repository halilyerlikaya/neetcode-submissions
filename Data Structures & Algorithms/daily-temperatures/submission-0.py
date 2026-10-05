class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stck  =[]
        for i ,t in enumerate(temperatures):
            while stck and t > stck[-1][0]:
                stckTemp , stckI  = stck.pop()
                res[stckI]  = i - stckI
            stck.append((t,i))
        return res
        