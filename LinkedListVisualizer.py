import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button
import tkinter as tk
from tkinter import simpledialog

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


    # Add a button to the current plot
    button_ax = plt.axes([0.81, 0.01, 0.1, 0.05])  # [left, bottom, width, height]
    button = Button(button_ax, 'Click Me')



    # plt.axis("off")
    button.on_clicked(on_button_click)


    # Show our network System
    plt.show()

def on_button_click(event):
    # Add a new node to the list
    linkedList.append(max(linkedList) + 1)

    # Clear the current plot
    plt.clf()

    # Update and redraw the graph with the new node
    LLVisualizer(linkedList, "double circular")

    # Redraw the plot
    plt.draw()


def get_user_input():
    # Create Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt user for input using a text box
    user_input = simpledialog.askstring("Input", "Enter text:")

    # Destroy the root window
    root.destroy()

    return user_input


if __name__ == '__main__':
    LLVisualizer(linkedList, "double circular")

    # Add a button to the current plot
    button_ax = plt.axes([0.81, 0.01, 0.1, 0.05])  # [left, bottom, width, height]
    button = Button(button_ax, 'Click Me')

    # Attach the button click event
    button.on_clicked(on_button_click)

    # Show the initial plot
    plt.show()

