from heapq import *; from collections import defaultdict

MOVES = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def diagonal_distance(cell, goal):
    dx = abs(cell[0] - goal[0])
    dy = abs(cell[1] - goal[1])
    return 1*(dx**2 + dy**2)**.5

def start_end_pos(wires):
    for i,x in enumerate(wires):
        if "S" in x: start = i,x.index('S')
        if "G" in x: end = i,x.index('G')
    return start, end


def wire_DHD_SG1(existingWires):
    wires = [list(x) for x in existingWires.splitlines()]
    end_X, end_Y = end = start_end_pos(wires)[0]
    start = start_end_pos(wires)[1]
    

    q = [(0, False, 0, start)]
    stored_cost = defaultdict(lambda:float('inf'))
    rebuilder = {}
    while q and not q[0][1]:
        h,check,cost,(x,y) = heappop(q)

        for (dx,dy) in MOVES:
            #movement trick for diagonal position either(1 or sqrt(2))
            new_cost = cost + (abs(dx) + abs(dy))**.5
            xx, yy = dx + x, dy + y

            if 0<=xx <len(wires) and 0<=yy<len(wires[0]) and new_cost < stored_cost[(xx,yy)] and wires[xx][yy]!='X':
                h = diagonal_distance((xx,yy), end)
                #if we push only cost into the heapq then we solve the problem by Best First Search!??
                heappush(q,(new_cost+h,(xx,yy)==end, new_cost,(xx,yy)))
                stored_cost[(xx,yy)] = new_cost
                rebuilder[(xx,yy)] = x,y
    
    if not q:
        return "Oh for crying out loud..."

    #REBUILDING PATH
    pos = rebuilder[end]
    while pos != start:
        x,y = pos
        wires[x][y] = 'P'
        pos = rebuilder[pos]

    return '\n'.join(''.join(x) for x in wires)





wires = """
.X.X.X....XXXXXX...X
XX.XX.XXXXXXXXXXX..X
.X.X.XX..X..X.XXXXXX
X.X..XXX...XX.X.XXX.
X.X..X..XXX.X.X.X...
.XXX..XXXXX.X.X..XX.
X.XX.SX......XXX..X.
.XXXXX.XXX...XX..X..
....X.XX..X.XX.X..XX
....X..XX..XX..X.XX.
X...X..XX.X.X.XX...X
.XXX.........X.XX..G
..XX.XX.XX.X.XXXXXX.
.X.X...X.X.XXXX..X.X
..X..XXX.XX....XXXX.
XX..XXXXXXX.....XXXX
XXXX.X.X..XXXXXX...X
X...X..X..XXXX..X..X
X.XXXXX..XX..XXX.X.X
XX.X.XX.XXXX.X..X.XX
""".strip('\n')

print(wire_DHD_SG1(wires))





