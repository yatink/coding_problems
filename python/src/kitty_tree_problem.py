# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

from collections import defaultdict
from itertools import combinations, count
from functools import lru_cache

def build_graph(pairs):
    # Represent the graph as a dict...each edge gets represented
    # in both [a] = b and [b] = a
    connections = defaultdict(list)
    for x,y in pairs:
        connections[x].append(y)
        connections[y].append(x)
    
    return connections

node_map = {}
counter = count()
    
def add_node(node_value, distance, hq):
    # Add the value to both the heapq and the
    # node_map. 
    if node_value in node_map:
        invalidate_node(node_value, hq)
    node_map[node_value] = [distance, next(counter), node_value]
    heapq.heappush(hq, node_map[node_value])

def invalidate_node(node_value, hq):
    # Mark the heapq entry as invalid by setting the
    # node value to None
    hq_entry = node_map.pop(node_value)
    hq_entry[-1] = None

def pop_node(hq):
    while hq:
        # Can raise IndexError
        dist, _, node_value = heapq.heappop(hq)
        if node_value is not None:
            del node_map[node_value]
            return node_value, dist
    raise IndexError("empty heap")    

    
paths = {}
def visit_node(curr_node, curr_dist, graph, hq, visited_nodes, heap_storage):
    # Visit all the neighbours...
    for neighbour in graph[curr_node]:
        if neighbour not in visited_nodes:
            dist, _, _ = heap_storage[neighbour]
            # Update distance of an unvisited node only if
            # it's distance is greater than what is calculated.
            if dist > curr_dist + 1:
                add_node(neighbour, curr_dist + 1, hq)
                paths[neighbour] = paths[curr_node] | {neighbour}
    visited_nodes[curr_node] = curr_dist
    

def djikstra(starting_node, graph):
    visited_nodes = {} # Node_name -> distance
    unvisited_nodes = [(1000000, x) for x in graph.keys() if x!= starting_node] # (distance, node_name) tuples
    unvisited_nodes.insert(0, (0, starting_node))
    unvisited_heap = []
    for dist, n in unvisited_nodes:
        add_node(n, dist, unvisited_heap)
        
    paths[starting_node] = {starting_node} 
    while unvisited_heap:
        # Get the node with the least distance from the
        # unvisited set
        try:
            node_value, dist = pop_node(unvisited_heap)
            visit_node(node_value, dist, graph, unvisited_heap, visited_nodes, node_map)
        except IndexError:
            pass
    #returns distances
    return visited_nodes, paths



    
@lru_cache(maxsize=None)
def calculate_pair(pair):
    u, v = pair
    # print(f'u: {u}, v: {v}, paths: {paths}')
    return u * v * len(paths[u] ^ paths[v])
    
def calculate(query):
    # print(f"Query: {query}")
    
    return sum(calculate_pair(tuple(sorted(q))) for q in query) % (10**9 + 7)


if __name__ == '__main__':
    f = open('./kitty_tree_problem.input')
    n, q = list(map(int, next(f).strip().split(' ')))
    edges = []
    first_node, second_node = list(map(int, next(f).strip().split(' ')))
    edges.append((first_node, second_node))
    for _ in range(n - 2):
        edges.append(tuple(map(int, next(f).strip().split(' '))))

    queries = []
    for _ in range(q):
        _ = int(next(f).strip())
        queries.append(list(map(int, next(f).strip().split(' '))))

    queries = [list(combinations(q, 2)) for q in queries]


    # Build the graph
    # print('Edges: ', edges)
    # print('queries: ', queries)
    graph = build_graph(edges)    
    # Run djikstraa on it to get node distances from the first node. 
    distances, paths = djikstra(first_node, graph)
    # print('Distances: ', distances)
    # print('Paths: ', paths)
    for query in queries:
        print(calculate(query))
