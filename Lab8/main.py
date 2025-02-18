import networkx as nx
import matplotlib.pyplot as plt

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
print("Սկզբնական կողեր:", edges)

edges = list(set(edges))
print("Կողեր կրկնվողները հեռացնելուց հետո:", edges)

G = nx.DiGraph()
G.add_edges_from(edges)

if nx.number_of_selfloops(G) > 0:
    print("Գրաֆում կան ինքնակապեր (self-loops):")
    print(list(nx.nodes_with_selfloops(G)))
    G.remove_edges_from(nx.selfloop_edges(G))

if not nx.is_tree(G):
    print("Գրաֆում կան ցիկլեր, դրանք չեն համապատասխանում ծառի հատկությանը:")
    G = nx.DiGraph(nx.minimum_spanning_tree(G.to_undirected()))
    print("Ցիկլերը հեռացվել են, գրաֆը դարձել է ծառ։")


def hierarchy_pos(G, root=1, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {}

    def _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter, pos, parent=None):
        neighbors = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            neighbors.remove(parent)
        if len(neighbors) != 0:
            dx = width / len(neighbors)
            nextx = xcenter - width / 2 - dx / 2
            for neighbor in neighbors:
                nextx += dx
                pos = _hierarchy_pos(
                    G,
                    neighbor,
                    width=dx,
                    vert_gap=vert_gap,
                    vert_loc=vert_loc - vert_gap,
                    xcenter=nextx,
                    pos=pos,
                    parent=root,
                )
        pos[root] = (xcenter, vert_loc)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter, pos)


def check_property_1(graph):
    return nx.number_of_selfloops(graph) == 0 and nx.is_tree(graph)


def check_property_2(graph):
    nodes = list(graph.nodes())
    return len(graph.edges()) == len(nodes) - 1


def check_property_3(graph):
    return nx.is_connected(graph.to_undirected())


def check_property_4(graph):
    for edge in graph.edges():
        graph_copy = graph.copy()
        graph_copy.remove_edge(*edge)
        if not nx.is_connected(graph_copy.to_undirected()):
            continue
        else:
            return False
    return True


def check_property_6(graph):
    return nx.is_bipartite(graph)


def check_property_7(graph):
    is_planar, _ = nx.check_planarity(graph)
    return is_planar


def check_property_8(graph):
    undirected_graph = graph.to_undirected()
    for node1 in undirected_graph.nodes():
        for node2 in undirected_graph.nodes():
            if node1 != node2:
                for node3 in undirected_graph.nodes():
                    if node1 != node3 and node2 != node3:
                        try:
                            path1 = nx.shortest_path(
                                undirected_graph, source=node1, target=node2
                            )
                            path2 = nx.shortest_path(
                                undirected_graph, source=node2, target=node3
                            )
                            path3 = nx.shortest_path(
                                undirected_graph, source=node1, target=node3
                            )
                        except nx.NetworkXNoPath:
                            continue

                        common_nodes = set(path1) & set(path2) & set(path3)
                        if len(common_nodes) > 1:
                            return False
    return True


def check_all_properties(graph):
    print(
        "Հատկություն 1. Ծառը չունի կրկնվող կողեր կամ հանգույցներ:",
        check_property_1(graph),
    )
    print(
        "Հատկություն 2. Ծառի ցանկացած n գագաթ պարունակող կառուցվածքում կա n-1 կող:",
        check_property_2(graph),
    )
    print(
        "Հատկություն 3. Ծառը վերջավոր կապված գրաֆ է, որը կապում է միայն մեկ պարզ շղթայով:",
        check_property_3(graph),
    )
    print("Հատկություն 4. Ծառի յուրաքանչյուր կող կամուրջ է:", check_property_4(graph))
    print("Հատկություն 6. Ծառը երկբաժան գրաֆ է:", check_property_6(graph))
    print("Հատկություն 7. Ծառը պլանար գրաֆ է:", check_property_7(graph))
    print(
        "Հատկություն 8. Ցանկացած երեք գագաթների համար ուղիները հատվում են միայն մեկ ընդհանուր գագաթում:",
        check_property_8(graph),
    )


pos = hierarchy_pos(G, root=1)
check_all_properties(G)

plt.figure(figsize=(8, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    font_size=12,
    node_color="lightblue",
    edge_color="black",
    arrows=True,
)
plt.title("Սորտավորված ծառի պատկեր")
plt.show()
