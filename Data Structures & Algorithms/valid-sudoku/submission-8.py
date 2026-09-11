class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                current = board[i][j]
                if current == ".":
                    continue
                b = (i // 3) * 3 + (j // 3)
                if current in rows[i] or current in cols[j] or current in boxes[b]:
                    return False
                rows[i].add(current)
                cols[j].add(current)
                boxes[b].add(current)
        return True
                        