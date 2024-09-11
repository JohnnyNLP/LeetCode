class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        m, n = len(land), len(land[0])

        def dfs(row, col) :
            if row >= m or col >= n or land[row][col] == 0 : return (0, 0)
            land[row][col] = 0

            r1, c1 = dfs(row+1, col) # expand to the right
            r2, c2 = dfs(row, col+1) # expand to the bottom
            h_r = max(r1, r2, row)
            h_c = max(c1, c2, col)

            return (h_r, h_c)

        for row_idx, row in enumerate(land):
            for col_idx, val in enumerate(row):
                if val == 1:
                    x, y = dfs(row_idx, col_idx)
                    result.append([row_idx, col_idx, x, y])

        return result