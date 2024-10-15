from collections import defaultdict

def read_graph_from_file(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as file:
        for line in file:
            u, v = map(int, line.split())
            graph[u].append(v)
            # Ensure all nodes are included in the graph
            if v not in graph:
                graph[v] = []
    return graph

def reverse_graph(graph):
    reversed_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            reversed_graph[v].append(u)
            if u not in reversed_graph:
                reversed_graph[u] = []
    return reversed_graph

def iterative_dfs(graph, start, visited, result):
    """Perform iterative DFS and collect the result."""
    stack = [start]
    component = []
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    result.append(component)

def kosaraju_scc(graph):
    visited = {key: False for key in graph}
    finish_stack = []

    for node in graph:
        if not visited[node]:
            stack = [node]
            while stack:
                curr_node = stack.pop()
                if curr_node < 0:
                    finish_stack.append(-curr_node)
                    continue
                if not visited[curr_node]:
                    visited[curr_node] = True
                    stack.append(-curr_node)
                    for neighbor in graph[curr_node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)

    reversed_graph = reverse_graph(graph)

    visited = {key: False for key in graph}
    scc = []

    while finish_stack:
        v = finish_stack.pop()
        if not visited[v]:
            iterative_dfs(reversed_graph, v, visited, scc)

    return scc

def main():
    graph = read_graph_from_file('problem8.10.txt')
    
    sccs = kosaraju_scc(graph)
    print("Strongly Connected Components:")

    sizes = [len(component) for component in sccs]

    largest_sizes = sorted(sizes, reverse=True)[:5]

    print("Largest 5 sizes of strongly connected components:", largest_sizes)

if __name__ == "__main__":
    main()