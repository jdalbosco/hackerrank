import collections

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

        
def make_graph(n_of_nodes, edges):
    graph = []
    
    for i in range(n_of_nodes):
        node = Node(i+1)
        graph.append(node)
        
    for first_node, second_node in edges:
        graph[first_node-1].neighbours.append(graph[second_node-1])
        graph[second_node-1].neighbours.append(graph[first_node-1])
    
    return graph

def calculate_distances_with_bfs(starting_node, n_of_nodes):
    visited = set()
    distances = [-1]*n_of_nodes
    queue = collections.deque()
    
    queue.append((starting_node, 0))
    while queue:
        current_node, distance = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            distances[current_node.value-1] = distance
            for neighbour in current_node.neighbours:
                queue.append((neighbour, distance+6))
                
    return distances

def get_distances(n_of_nodes, edges, starting_node_value):
    graph = make_graph(n_of_nodes, edges)
    starting_node = graph[starting_node_value-1]
    
    distances = calculate_distances_with_bfs(starting_node, n_of_nodes)
    distances.remove(0)
    
    return distances