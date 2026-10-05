class Solution:
    def maxArea(self, height: List[int]) -> int:
        i ,j =  0 , len(height) -1 
        maxer  = 0 
        while i < j: 
            maxer  = max( maxer, (j-i )* min(height[i], height[j]))
            if height[i] < height [j]:
                i += 1 
            else:
                j -= 1
        return maxer