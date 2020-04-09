from collections import deque

MOVES = ((-1, 0), (1, 0), (0, -1), (0, 1))
def path_finder(maze):
    maze = [list(x) for x in maze.split('\n')]
    start_node = x,y = (0,0)
    queue = deque()
    queue.append( (x,y) )
    end_node = len(maze)-1, len(maze)-1
    
    path_builder = {}
    while queue:
        x,y = queue.popleft()

        if (x,y) == end_node:
            break       

        for dx,dy in MOVES:
            xx, yy = dx+x, dy+y

            if 0 <=xx<len(maze) and 0<=yy<len(maze[0]) and maze[xx][yy] != 'W':
                    queue.append((xx, yy))
                    maze[xx][yy] = 'W'
                    path_builder[xx,yy] = x,y


    if not queue and (x,y) != end_node: return False

    #rebuilding the path
    pos, full_path = end_node, []
    while not full_path or full_path[-1] != start_node:
        full_path.append(pos)
        pos = path_builder[pos]

    return full_path[::-1]



c = "\n".join([
  "...",
  "W..",
  ".W."])

print(path_finder(c))