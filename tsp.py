from sys import maxsize
import time
from itertools import permutations
from distance import matrix
V = 8
 
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    count_perm = 0
    for i in next_permutation:
        count_perm += 1
 
        current_pathweight = 0
        k = s
        print(i)
        # compute current path weight
        for j in i:
            current_pathweight += graph[k][j]
            print(k,j)
            k = j
        current_pathweight += graph[k][s]
        print(k,s)
        print(current_pathweight)
 
        # update minimum
        min_path = min(min_path, current_pathweight)

    #print(count_perm)
    print(f'permutações = {count_perm}')
    return min_path

start_time = time.time() 
if __name__ == "__main__":
 
    graph = matrix()
    s = 0
    print(travellingSalesmanProblem(graph, s))
print("--- %s seconds ---" % (time.time() - start_time))
