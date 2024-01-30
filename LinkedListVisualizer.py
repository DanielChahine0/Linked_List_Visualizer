import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button

linkedList = [1, 2, 3, 4, 5, 6]


def LLVisualizer(l_list, link_type):
    N = nx.DiGraph()

    # Add all the nodes
    N.add_nodes_from(l_list)

    # If our list is a Singly-Linked List
    if link_type == "singly":
        for i in range(len(l_list)-1):
            from_node = l_list[i]
            to_node = l_list[i+1]
            N.add_edge(from_node, to_node)

    # If our list is a Circular-Linked List
    elif link_type == "circular":
        N.add_edge( l_list[len(l_list)-1], l_list[0])
        for i in range(len(l_list)-1):
            from_node = l_list[i]
            to_node = l_list[i+1]
            N.add_edge(from_node, to_node)

    # If our list is a Doubly-Linked List
    elif link_type == "double":
        for i in range(len(l_list)-1):
            from_node = l_list[i]
            to_node = l_list[i+1]
            N.add_edge(from_node, to_node)
            N.add_edge(to_node, from_node)

    # If our list is a Circular Doubly-Linked List
    elif link_type == "double circular":
        N.add_edge(l_list[len(l_list) - 1], l_list[0])
        N.add_edge(l_list[0], l_list[len(l_list) - 1])
        for i in range(len(l_list) - 1):
            from_node = l_list[i]
            to_node = l_list[i + 1]
            N.add_edge(from_node, to_node)
            N.add_edge(to_node, from_node)

    # Configure the position of our nodes to be in a circle
    position = nx.circular_layout(N)

    # Display our nodes on our network
    nx.draw_networkx_nodes(N, position, node_size=500, node_color="red")

    # Display the edges of our nodes on the network
    nx.draw_networkx_edges(N, position)

    # Display the value of our nodes
    nx.draw_networkx_labels(N, position, font_size=5, font_color="white")

    # plt.axis("off")
    fig, ax = plt.subplots()
    axnext = fig.add_axes([0.51, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')

    # Show our network System
    plt.show()


if __name__ == '__main__':
    LLVisualizer(linkedList, "double circular")

