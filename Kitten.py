from collections import deque

kitten_p = int(input())
path = []
start = 0

# Create hash map and store neighbors
tree_hash = {}
while True:
    line = input().strip()                       
    if line == "-1":                             
        break                                    
    connection = list(map(int, line.split()))   
    tree_hash[connection[0]] = connection[1:]   

# Find bottom of tree (source in the directed graph)
start = set(tree_hash.keys())                   
values = set()
for v in tree_hash.values():       
    values.update(v)                             
start_keys = start - values                      
bottom = next(iter(start_keys))            

# Run BFS shortest path
def BFS_shortest_path(tree_hash, bottom, kitten_p): 
    visited = set()
    queue = deque([[bottom]])     

    if bottom == kitten_p:
        return [bottom]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbours = tree_hash.get(node, [])

            for neighbor in neighbours:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == kitten_p:
                    return new_path
            visited.add(node)
    return None

flip = BFS_shortest_path(tree_hash, bottom, kitten_p)
sol = flip[::-1]
for n in sol:
    print(n, end = " ")

