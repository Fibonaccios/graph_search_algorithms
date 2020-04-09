from heapq import heappush, heappop
from collections import defaultdict

def MST(graph, start):
    total_cost = 0                   
    seen = set()
    mst = defaultdict(list)
    queue = [(0, start, start)]
    while queue:
        cost, node, parent_node = heappop(queue)

        if node not in seen:
            seen.add(node)
            if cost:
                total_cost += cost

                mst[parent_node].append({node:cost})

            for neighbour, cost in graph[node].items():
                if neighbour not in seen:
                    heappush(queue, (cost, neighbour, node))

    return f'MST --> {mst} \nCOST: {total_cost}'


example_graph = {
    'A': {'B': 5, 'D':9, 'E':1},
    'B': {'A': 5, 'C': 5, 'E':1},
    'C': {'D':2, 'B': 5, 'E':1},
    'D': {'A':9, 'C':2, 'E':1},
    'E': (dict(zip('ABCD',[1,1,1,1])))
    }

print(MST(example_graph, 'A'))

