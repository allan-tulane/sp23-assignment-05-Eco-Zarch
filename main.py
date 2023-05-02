from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        next_frontier = set()
        for node in frontier:
            for neighbor in graph[node]:
                if neighbor not in result:
                    result.add(neighbor)
                    next_frontier.add(neighbor)
        frontier = next_frontier
    return result

def connected(graph):
    visited_nodes = set()
    for node in graph:
        if node not in visited_nodes:
            connected_nodes = reachable(graph, node)
            visited_nodes.update(connected_nodes)
            if len(visited_nodes) != len(graph):
                return False
            return True
    return True

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    visited_nodes = set()
    components = 0

    for node in graph:
        if node not in visited_nodes:
            connected_nodes = reachable(graph, node)
            visited_nodes.update(connected_nodes)
            components += 1
    return components

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2


test_reachable()
test_connected()
test_n_components()
