import networkx as nx
import numpy as np
# import matplotlib.pyplot as plt
import random


G = nx.erdos_renyi_graph(20, 0.15, directed = True)

# nx.draw_spring(G)
# plt.show()

nx.draw(G, with_labels = True)

# idea: create graph and copy graph and make slight adjustments, compare both embeddings and caclulate distance


# adjust signature for graph type

def random_walk(graph, start_node:int = 0, walk_length:int = 1) -> list[int]:

    sequence = [start_node]

    print(f"{walk_length} xxx")

    for _ in range(walk_length):
        neighbours = [neighbour for neighbour in graph.neighbors(start_node)]
        print()
        print(start_node)
        print(neighbours)
        print()
        if neighbours == []:
          return sequence
        selected_neighbour = random.choice(neighbours)
        sequence.append(selected_neighbour)
        start_node = selected_neighbour
    return sequence

for _ in range(5):
    print(random_walk(G, random.randrange(20), random.randrange(4,10)))
