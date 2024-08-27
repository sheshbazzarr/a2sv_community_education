class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Create sets for walls and guards
        walls_set = {(r, c) for r, c in walls}
        guards_set = {(r, c) for r, c in guards}
        
        # Set to track guarded cells
        guarded = set()
        
        # Direction vectors: (row_offset, col_offset)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # North, South, West, East
            
            # Function to simulate guard vision in one direction
        def simulate_guard(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if (r, c) in walls_set or (r, c) in guards_set:
                    break
                guarded.add((r, c))
                r += dr
                c += dc
        
        # Simulate for each guard
        for r, c in guards:
            for dr, dc in directions:
                simulate_guard(r + dr, c + dc, dr, dc)
        
        # Count unguarded and unoccupied cells
        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in guarded and (r, c) not in walls_set and (r, c) not in guards_set:
                    unguarded_count += 1
        
        return unguarded_count
