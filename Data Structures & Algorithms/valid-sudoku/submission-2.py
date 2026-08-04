class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #input - matrix of matrix,output-bool
        #brute force - for each row and col check by for loop
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue
                if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3, c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    square[(r//3,c//3)].add(board[r][c])
        return True

        