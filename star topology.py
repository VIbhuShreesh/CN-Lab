import matplotlib.pyplot as plt
import networkx as nx

def draw_star_topology():
    # Create a star graph with a central hub (node 0)
    G = nx.Graph()
    devices = ['A', 'B', 'C', 'D']
    hub = 'Hub'

    positions = {
        'A': (-1, 1),
        'B': (1, 1),
        'C': (-1, -1),
        'D': (1, -1),
        'Hub': (0, 0)
    }

    G.add_node(hub)
    for device in devices:
        G.add_node(device)
        G.add_edge(hub, device)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos=positions, node_color='skyblue', node_size=1000)
    # Draw edges
    nx.draw_networkx_edges(G, pos=positions, width=2)
    # Draw labels
    nx.draw_networkx_labels(G, pos=positions, font_size=12, font_weight='bold')

    # Add arrow for communication from A -> B via Hub
    plt.arrow(-1, 1, 0.5, -1, head_width=0.1, color='red')  # A to Hub
    plt.arrow(0, 0, 0.8, 1, head_width=0.1, color='red')   # Hub to B

    plt.title("Star Topology - A sends data to B via Hub", fontsize=14)
    plt.axis('off')
    plt.show()

draw_star_topology()