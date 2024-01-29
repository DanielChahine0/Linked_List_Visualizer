import matplotlib.pyplot as plt
import networkx as nx

def visualize_turing_machine(states, transitions):
    G = nx.DiGraph()

    # Add nodes for states
    G.add_nodes_from(states)

    # Add edges for transitions
    for transition in transitions:
        from_state, to_state, read_symbol, write_symbol, move_direction = transition
        G.add_edge(from_state, to_state, label=f"{read_symbol}/{write_symbol}, {move_direction}")

    pos = nx.spring_layout(G)  # You can use other layout algorithms

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")

    # Draw edges
    nx.draw_networkx_edges(G, pos)

    # Draw edge labels
    edge_labels = {(from_state, to_state): label for (from_state, to_state, label) in G.edges(data='label')}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

    plt.axis("off")
    plt.show()

# Example Turing machine states and transitions
tm_states = ['q0', 'q1', 'q2', 'q3']
tm_transitions = [
    ('q0', 'q1', '0', '1', 'R'),
    ('q1', 'q2', '1', '0', 'L'),
    ('q2', 'q3', '0', '1', 'R'),
]

# Visualize the Turing machine
visualize_turing_machine(tm_states, tm_transitions)
