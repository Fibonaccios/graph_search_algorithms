from collections import deque

def graph(maze):
    maze = [list(x) for x in maze.split('\n')]
    maze[0][0] = 'W'

    x,y = 0,0
    graph = {}
    queue = deque()
    queue.append((x,y))

    while queue:
        current_pos = queue.popleft() #BFS   for   DFS queue.pop()
            
        for x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = current_pos[0] + x[0]
            yy = current_pos[1] + x[1]

            if (xx >= 0 and xx < len(maze) and yy >= 0 and yy < len(maze)):
                if maze[xx][yy] != 'W':
                    queue.append((xx, yy))
                    maze[xx][yy] = 'W'
                    graph.setdefault(current_pos, []).append((xx,yy))
                
    return graph


a = "\n".join([
  "...",
  ".W.",
  "..."
])

print(graph(a))