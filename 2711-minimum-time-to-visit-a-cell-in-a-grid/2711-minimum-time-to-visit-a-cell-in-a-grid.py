class Solution:
    def minimumTime(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Check if it's impossible to reach the destination from the start
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        time = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        vis = [[0] * (n + 1) for _ in range(m + 1)]

        pq = []
        heapq.heappush(pq, (0, (0, 0)))  # Start from the top-left corner

        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]

        while pq:
            t, (curx, cury) = heapq.heappop(pq)

            # Return time if we reach the bottom-right corner
            if curx == m - 1 and cury == n - 1:
                return t

            if vis[curx][cury]:
                continue
            vis[curx][cury] = 1

            for i in range(4):
                newx = curx + x[i]
                newy = cury + y[i]

                if 0 <= newx < m and 0 <= newy < n:
                    needtime = t + 1

                    # Adjust time based on grid values
                    if grid[newx][newy] > t + 1:
                        diff = grid[newx][newy] - t
                        needtime = grid[newx][newy] if diff % 2 else grid[newx][newy] + 1

                    if needtime < time[newx][newy]:
                        time[newx][newy] = needtime
                        heapq.heappush(pq, (needtime, (newx, newy)))

        return -1