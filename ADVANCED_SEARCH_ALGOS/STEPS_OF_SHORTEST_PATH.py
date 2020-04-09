a = "\n".join([
  "...",
  ".W.",
  "..."
])


def path_finder(maze):
    maze = maze.split('\n')
    row, col = len(maze[0]), len(maze)
    start = (0, 0)
    end = (row - 1, col - 1)
    q = [start]
    visited_at = {start: 0}
    
    while q:
        x, y = q.pop(0) #parent node!

        if (x, y) == end:
            return visited_at[end]
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = x + dx
            yy = y + dy
            if ((xx, yy) not in visited_at and 0 <= xx < row ) and (0 <= yy < col and maze[xx][yy] == '.'):
                q.append((xx, yy))
                visited_at[(xx, yy)] = visited_at[(x, y)] + 1
            
    return False

print(path_finder(a))