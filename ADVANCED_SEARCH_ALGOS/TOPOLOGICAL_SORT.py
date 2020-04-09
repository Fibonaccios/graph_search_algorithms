def iterative_topological_sort(graph, start):
    seen = set()
    stack = []    # path variable is gone, stack and order are new
    order = []    # order will be in reverse order at first
    q = [start]
    while q:
        node = q.pop()
        if node not in seen:
            seen.add(node) # no need to append to path any more
            q.extend(graph[node])

            while stack and node not in graph[stack[-1]]: # new stuff here!
                order.append(stack.pop())
            stack.append(node)

    return stack + order[::-1]   # new return value!


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}



def iterative_topological_sort(graph, start):
    queue = [start]
    path = set()
    top_sort = []

    while queue:
        node = queue[-1]                   #item 1,just access, don't pop
        path = path.union({node})
        children = [x for x in graph[node] if x not in path]

        if not children:                   #no child or all of them already visited.
            top_sort = [node]+top_sort 
            queue.pop()
        else:
            queue.append(children[0])   #item 2, push just one child

    return top_sort


print(iterative_topological_sort(graph, 'a'))