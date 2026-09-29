import random
import heapq


grid = [[random.randint(1, 9) for j in range(4)] for i in range(4)]
print("Risk Grid:")
for row in grid:
    print(row)

start = (0, 0)
goal = (3, 3)


pq = [(grid[0][0], start, [start])]
visited = set()

while pq:
    cost, pos, path = heapq.heappop(pq)

    if pos in visited:
        continue
    visited.add(pos)

    if pos == goal:
        print("Lowest Risk:", cost)
        print("Path:", path)

        health = 100
        print("Health:", health)
        for p in path:
            health -= grid[p[0]][p[1]]
            print(p, "Health =", health)
        break

    r, c = pos
    for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
        if 0 <= nr < 4 and 0 <= nc < 4:
            heapq.heappush(
                pq, (cost + grid[nr][nc], (nr, nc), path + [(nr, nc)])
            )
