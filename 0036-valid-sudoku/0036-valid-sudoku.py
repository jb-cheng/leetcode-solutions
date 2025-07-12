class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subboxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]

                # Skip '.'s
                if element == '.':
                    continue
            
                if element in rows[i] or element in cols[j] or element in subboxes[3 * (i//3) + j//3]:
                    return False
                else:
                    rows[i].add(element)
                    cols[j].add(element)
                    subboxes[3 * (i//3) + j//3].add(element)

        return True