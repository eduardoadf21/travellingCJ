
from sys import maxsize
import time
from itertools import permutations
from distance import generate_graph
V = 8
 
def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        min_path = min(min_path, current_pathweight)

    return min_path

start_time = time.time() 
if __name__ == "__main__":
 
    graph = generate_graph()
    s = 0
    print(travellingSalesmanProblem(graph, s))
print("--- %s seconds ---" % (time.time() - start_time))
