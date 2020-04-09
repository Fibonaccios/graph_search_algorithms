graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [10],
    4: [7, 8],
    5: [9, 10],
    7: [11, 12],
    11: [13]
}


def bfs1(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # Mark the vertex as visited
            visited.add(vertex)
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

print(bfs1(graph,1, 11))


tree2 = {
    0: {'colour': 'white', 'neighbours': [1, 2]},
    1: {'colour': 'white', 'neighbours': [0, 3, 4]},
    2: {'colour': 'white', 'neighbours': [0, 5, 6]},
    3: {'colour': 'white', 'neighbours': [1]},
    4: {'colour': 'white', 'neighbours': [1]},
    5: {'colour': 'white', 'neighbours': [2, 9]},
    6: {'colour': 'white', 'neighbours': [2, 7, 8]},
    7: {'colour': 'white', 'neighbours': [6]},
    8: {'colour': 'white', 'neighbours': [6, 10]},
    9: {'colour': 'white', 'neighbours': [5]},
    10:{'colour': 'white', 'neighbours': [8]}}

def bfs2(vertex, graph, end):
    q = [(vertex, [])]
    steps = 0

    while q:
        vertex, path = q.pop(0)
        path = path + [vertex]

        if vertex == end:
            return path, len(path)
        
        else:
            if graph[vertex]['colour'] == 'white':
                graph[vertex]['colour'] = 'black'

                for x in graph[vertex]['neighbours']:
                    if graph[x]['colour'] != 'black':
                        q.append((x, path))
    return path

print(bfs2(4, tree2, 10))