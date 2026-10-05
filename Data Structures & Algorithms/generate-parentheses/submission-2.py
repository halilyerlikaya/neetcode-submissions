def backtrack(open:int,closed:int,n :int,curr:str):
        son  = []
        if closed == open == n:
            return [curr]
        if open < n:
            son += backtrack(open+1,closed,n,curr+"(")
        if open > closed:
            son += backtrack(open,closed+1,n,curr+")")
        return son
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = backtrack(0,0,n,"")
        return res


