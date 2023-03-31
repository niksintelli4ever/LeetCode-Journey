class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        M = (10**9) + 7
        rows = len(pizza)
        cols = len(pizza[0])

        # create suffixSum
        suffixSum = [[0] * cols for i in range(rows)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                suffixSum[i][j] = (
                    (1 if pizza[i][j] == "A" else 0)
                    + (suffixSum[i + 1][j] if i + 1 < rows else 0)
                    + (suffixSum[i][j + 1] if j + 1 < cols else 0)
                    - (suffixSum[i + 1][j + 1] if i + 1 < rows and j + 1 < cols else 0)
                )

        @cache
        def countWays(x, y, cuts):
            if cuts == 0:
                return 1

            count = 0

            # divide horizontally
            for i in range(x, rows - 1):
                if (
                    suffixSum[i + 1][y] != 0
                    and (suffixSum[x][y] - suffixSum[i + 1][y]) != 0
                ):
                    count += countWays(i + 1, y, cuts - 1)

            # divide vertically
            for j in range(y, cols - 1):
                if (
                    suffixSum[x][j + 1] != 0
                    and (suffixSum[x][y] - suffixSum[x][j + 1]) != 0
                ):
                    count += countWays(x, j + 1, cuts - 1)

            return count % M

        return countWays(0, 0, k - 1)