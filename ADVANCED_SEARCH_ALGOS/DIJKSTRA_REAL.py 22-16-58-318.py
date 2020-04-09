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




# THE REAL DIJKSTRA!!
def dijkstra(graph, starting_vertex):
    all_distances = defaultdict(lambda:float('inf'))
    all_distances[starting_vertex] = 0

    queue = [(0, starting_vertex)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue because if processed again
        # the total distance would be greater since we go beyond that node.
        # IF THE CURRENT DISTANCE FROM SOURCE > THE DISTANCE WE HAVE STORED WE RETURN TO WHILE LOOP!
        if current_distance > all_distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight

            # Only consider this new path if it's better than any path we've already found.
            if new_distance < all_distances[neighbor]:
                all_distances[neighbor] = new_distance
                #we push the new DISTANCE FROM SOURCE
                heapq.heappush(queue, (new_distance, neighbor))

    return all_distances

print(dijkstra(graph, 'a'))




# ''' DIJKSTRA SPF WITH A SLIGHT MODIFICATION ON RETURNING THE COST/PATH FROM A NODE TO ANOTHER
#     IF end == True else RETURNS THE SHORTEST PATH FROM A STARTING VERTEX TO ALL VERTICES!'''
# def calculate_distances(graph, starting_vertex, ending_vertex):
#     all_distances = {vertex: float('infinity') for vertex in graph}
#     all_distances[starting_vertex] = 0

#     queue = [(0, starting_vertex, [])]
#     while queue:
#         current_distance, current_vertex, path = heapq.heappop(queue)
#         path = path + [current_vertex]

#         # Nodes can get added to the priority queue multiple times. We only
#         # process a vertex the first time we remove it from the priority queue.
#         # if current_distance > all_distances[current_vertex]:
#         #     continue
    
#         #Returning cost of shortest path between starting_vertex and ending vertex
#         #Since current vertex == end: then we exhausted all the ways to get there and we don't need
#         #to go beyond that.
#         if current_vertex == ending_vertex:
#             return all_distances[ending_vertex]

#         for neighbour, weight in graph[current_vertex].items():
#             new_distance = current_distance + weight

#             # Only consider this new path if it's better than any path we've
#             # already found.
#             if new_distance < all_distances[neighbour]:
#                 all_distances[neighbour] = new_distance
#                 heapq.heappush(queue, ((new_distance, neighbour, path)))

#     return False

# print(calculate_distances(graph, 'a', 'b'))