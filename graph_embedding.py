# -*- coding: utf-8 -*- 
"""graph_embedding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Co_aofH5liRg-xLdCBJpP0F0w16SkrsM
"""

# Import required packages

import networkx as nx
import random
#%pip install gensim
from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
import time

# Create and draw graph

n = 10
p = 0.25

G = nx.erdos_renyi_graph(n, p, directed = True)

# outdated version
# nx.draw(G, with_labels = True)

nx.draw_networkx(G, with_labels = True)
plt.show()

# perform random walks in graph

def random_walk(graph:nx.Graph, start_node:int = 0, walk_length:int = 1) -> list[int]:

    sequence = [str(start_node)]

    for _ in range(walk_length):
        neighbours = [neighbour for neighbour in graph.neighbors(start_node)]
        if neighbours == []:
          return sequence
        selected_neighbour = random.choice(neighbours)
        sequence.append(str(selected_neighbour))
        start_node = selected_neighbour

    return sequence

# example of random walks in graph
for _ in range(5):
    print(random_walk(G, random.randrange(n), 10))

# create walks for Word2Vec

amount_walks = 200
length_per_walk = 20
dimension = 2

walks = []

for _ in range(amount_walks):
  walks.append(random_walk(G, random.randrange(n), length_per_walk))


# Train Word2Vec model, play around with Word2Vec hyperparameters

model = Word2Vec(walks, vector_size = dimension, window = 2, sg = 1, min_count = 1)
model.train(walks, total_examples = model.corpus_count, epochs = 30, report_delay = 1)

# show results of node embedding

for node in range(n):
  print(f"Node {node:2d}: {model.wv.get_vector(node)}")

"""
# compare to DeepWalk implementation from Karateclub

karate_model = DeepWalk(walk_length = length_per_walk, dimensions = dimension, window_size = 2)
karate_model.fit(G)
karate_embedding = karate_model.get_embedding()

for node in range(n):
  print(f"Node {node:2d}: {karate_embedding[node]}")
  """

# testing for similarity of nodes

input_number = 0

while input_number != -1:
  input_number = int(input("Similarity to which node would you like to check (enter -1 to exit): "))
  if input_number != -1:
    for node_details in model.wv.most_similar(positive = [input_number]):
      print(node_details)
    print()
    time.sleep(5)
