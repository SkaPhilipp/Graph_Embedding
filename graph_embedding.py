import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random


G = nx.erdos_renyi_graph(20, 0.05)

nx.draw_spring(G)
plt.show()


# idea: create graph and copy graph and make slight adjustments, compare both embeddings and caclulate distance


# adjust signature for graph type

def random_walk(graph, start_node:int = 0, walk_length:int = 1) -> list[int]:
    
    sequence = [start_node]

    for _ in range(walk_length):
        neighbours = [neighbour for neighbour in graph.neighbors(start_node)]
        selected_neighbour = random.choice(neighbours)
        sequence.append(selected_neighbour)
        start_node = selected_neighbour
    return sequence

for _ in range(5):
    print(random_walk(G, random.randrange(20), random.ranrange(2,8)))

