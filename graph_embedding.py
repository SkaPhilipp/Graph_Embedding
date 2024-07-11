import networkx as nx
import random
from gensim.models import Word2Vec
import time

n = 20
p = 0.15

G = nx.erdos_renyi_graph(n, p, directed = True)

nx.draw(G, with_labels = True)

# idea: 
# create graph and copy graph and make slight adjustments, compare both embeddings and caclulate distance
# have block using skipgram and alternative block using skipgram implementation from scratch

# adjust signature for graph type

def random_walk(graph, start_node:int = 0, walk_length:int = 1) -> list[int]:

    sequence = [start_node]

    for _ in range(walk_length):
        neighbours = [neighbour for neighbour in graph.neighbors(start_node)]
        if neighbours == []:
          return sequence
        selected_neighbour = random.choice(neighbours)
        sequence.append(selected_neighbour)
        start_node = selected_neighbour

    return sequence

# example of random walks in graph
for _ in range(5):
    print(random_walk(G, random.randrange(20), random.randrange(4,10)))

# create walks for Word2Vec

amount_walks = 200
length_per_walk = 20

walks = []

for _ in range(amount_walks):
  walks.append(random_walk(G, random.randrange(n), length_per_walk))


# play around with Word2Vec hyperparameters

skip_gram = Word2Vec(walks, vector_size = amount_walks, window = 2, sg = 1, min_count = 1)
skip_gram.train(walks, total_examples = skip_gram.corpus_count, epochs = 30, report_delay = 1)


# testing / add clr screen, etc to it

input_number = 0

while input_number != -1:
  input_number = int(input("Similarity to which node would you like to check (enter -1 to exit): "))
  if input_number != -1:
    for node_details in skip_gram.wv.most_similar(positive = [input_number]):
      print(node_details)
    print()
    time.sleep(5)
