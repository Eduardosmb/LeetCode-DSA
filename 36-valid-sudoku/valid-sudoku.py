class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # col = defaultdict(list)
        # line = defaultdict(list)

        # for l in range(len(board)):
        #     for c in range(len(board)):
        #         if board[l][c] != '.':
        #             if board[l][c] not in col[c] and board[l][c] not in line[l]:
        #                 col[c].append(board[l][c])
        #                 line[l].append(board[l][c])
        #             else:
        #                 return False
        # return True


        col = defaultdict(set)
        line = defaultdict(set)
        square = defaultdict(set)

        for l in range(9):
            for c in range(9):
                if board[l][c] != '.':
                    if (board[l][c] in col[c]) or (board[l][c] in line[l]) or board[l][c] in square[(l//3, c//3)]:
                        return False

                    col[c].add(board[l][c])
                    line[l].add(board[l][c])
                    square[(l//3, c//3)].add(board[l][c])
        return True

