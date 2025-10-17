
#input
N, M = map(int, input().split())
rows = [input().strip() for _ in range(N)]

# Build grid of 0's outside of original grid, and add original grid
padded = [[0] * (M + 2) for _ in range(N + 2)]
for i in range(N):
    for j in range(M):
        padded[i + 1][j + 1] = 1 if rows[i][j] == '1' else 0

visited = [[False] * (M + 2) for _ in range(N + 2)]

# Neighbours
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Start DFS from (0,0)
stack = [(0, 0)]
visited[0][0] = True

coastline = 0

# DFS ocean seach, and count land edges

while stack:
    i, j = stack.pop()
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < N + 2 and 0 <= nj < M + 2: 
            if padded[ni][nj] == 1:  # If neighbor is land
                coastline += 1
            else:                      # If neighbor is water
                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    stack.append((ni, nj))


print(coastline)