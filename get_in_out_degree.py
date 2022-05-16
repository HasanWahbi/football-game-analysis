import networkx as nx

def getInDegree(graph, node):
    in_degree = 0
    for edge in graph.in_edges(node):
        in_degree += graph.get_edge_data(edge[0], edge[1])['weight']
    return in_degree


def getOutDegree(graph, node):
    out_degree = 0
    for edge in graph.out_edges(node):
        out_degree += graph.get_edge_data(edge[0], edge[1])['weight']
    return out_degree


def getPerformance(graph, property = 'name'):
    perfomance = []
    for node in graph.nodes(data=True):
        out_degree = getOutDegree(graph, node[0])
        in_degree = getInDegree(graph, node[0])
        perfomance.append({
             node[1][property]: out_degree - in_degree
        })
    for player in perfomance:
        print(f'{list(player.items())[0][0]}: {list(player.items())[0][1]}')

    return perfomance



