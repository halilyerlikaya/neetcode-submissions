class Solution:
    def bst(self,col : List[int],target: int) -> bool:
        start ,end  = 0 , len(col) -1 
        while end >= start:
            i  = start + (end-start)//2
            if col[i] == target:
                return True
            elif col[i] > target:
                end  = i -1 
            else:
                start =  i + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = []
        for row in matrix:
            col += row
        return self.bst(col,target)
