class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        yatay = defaultdict(set)
        dikey = defaultdict(set)
        kume = defaultdict(set)
        for y in range(9):
            for x in range(9):
                if board[x][y] == "." :
                    continue
                if(board[x][y] in dikey[y] or board[x][y] in yatay[x] 
                    or board[x][y] in kume[(x//3,y//3)]):
                    return False
                dikey[y].add(board[x][y])
                yatay[x].add(board[x][y])
                kume[(x//3,y//3)].add(board[x][y])
        return True