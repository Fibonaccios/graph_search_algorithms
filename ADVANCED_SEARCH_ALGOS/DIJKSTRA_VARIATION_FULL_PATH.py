import heapq
from collections import defaultdict

graph = {
'a': {'w': 14, 'x': 7, 'y': 9},
'b': {'w': 9, 'z': 6},
'w': {'a': 14, 'b': 9, 'y': 2},
'x': {'a': 7, 'y': 10, 'z': 15},
'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
'z': {'b': 6, 'x': 15, 'y': 11},
}

'''A VARIATION OF DIJKSTRA FINDING THE SHORTEST COST AND PATH FROM A NODE TO ANOTHER ONE'''
def shortest_path(graph, start, end_node):
    all_distances = defaultdict(lambda:float('inf'))
    all_distances[start] = 0    
    queue = [(0, start)]
    path = {}

    while queue:
        distance, node = heapq.heappop(queue)

        #end node was found no point going beyond it.
        if node == end_node:
            #if we want to just return the total shortest path from start_node to end_node.
            #return all_distances[end_node]
            break

        for (v, cost) in graph[node].items():
            new_distance = distance + cost

            #extracting all paths from end node to ---> (start node)
            if new_distance < all_distances[v]:
                all_distances[v] = new_distance
                heapq.heappush(queue, (new_distance, v))
                path[v] = node


    shortest_path = []
    #return shortest_path from node to node with their edge weight(cost)
    while end_node != start:
        edge_distance = all_distances[end_node] - all_distances[path[end_node]]
        shortest_path.append({(path[end_node], end_node): edge_distance})
        end_node = path[end_node]
    return shortest_path[::-1]

print(shortest_path(graph,'a', 'b'))
#z y a 