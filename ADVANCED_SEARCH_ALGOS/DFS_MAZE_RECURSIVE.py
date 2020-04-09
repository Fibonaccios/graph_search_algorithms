
def path_finder(maze, v, seen, all_paths):

    if v == (len(maze)-1, len(maze)-1):
        return True

    x,y = v
    if (x,y) not in seen:
        seen.add((x,y))
        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = x + dx
            yy = y + dy

            if (xx >= 0 and xx < len(maze) and yy >= 0 and yy < len(maze) and (xx,yy) not in seen):
                if maze[xx][yy] != 'W':
                    if path_finder(maze, (xx,yy), seen, all_paths):
                        all_paths.append((xx,yy))
                        return all_paths
    return False

c = "\n".join([
  "...",
  "..W",
  "..."])

m = [list(x) for x in c.split('\n')]
print(path_finder(m, (0,0), set(), list()))