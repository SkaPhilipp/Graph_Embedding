# Graph_embedding


This is a toy project with a Python implementation of the graph embedding algorithm Deepwalk using networkx for graph generation.

------ ENTER MORE TEXT -----------

We use networkx to create a directed graph as shown below:

-------- USE CSS AND HTML TO BEAUTIFY README -----------

![Example of directed graph](./digraph.JPG)

Next, we perform multiple random walks in the graph as illustrated in the following examples of length 10:

'''
[4, 7, 0, 2, 3, 1, 4, 7, 0, 2, 4]
[1, 4, 7, 0, 2, 6, 5, 8, 9, 0, 2]
[5, 4, 7, 0, 2, 6, 9, 6, 5, 8, 7]
[1, 0, 2, 3, 8, 3, 8, 7, 0, 2, 6]
[3, 1, 8, 3, 8, 3, 1, 8, 6, 5, 8]
'''

Then we use Word2Vec from gensim to create a graph embedding.

-------- INSERT IMAGE OF NODE EMBEDDING --------

Discuss entering node to check for similarity

-------- INSERT IMAGE OF PROMPT -------

Discuss further ideas:

- alteration to graph and compare embeddings / distance
- use alternative to Word2Vec / algorithm from scratch (G4G)
- improve random walk
- use deepwalk in graph with real-world data in separate file (similarity interesting)
- use embedding in ML task
- comparison to DeepWalk implementation from Karateclub in separate file
