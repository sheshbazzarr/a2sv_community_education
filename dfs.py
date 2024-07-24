def dfs(verted,visited):
    # base case

    visited.add(verted)
    for neighbour in graph[verted]:
        if neighbour not in visited:
            dfs(neighbour,visited)
