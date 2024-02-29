import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
def min_k_for_Bk(A):
   
    B = A.copy()  
    k = 1  
    
    while True:
        if np.all(B >= 1):  
            return k
        k += 1  
        A_k = np.linalg.matrix_power(A, k)  
        B += A_k  

# 示例
A = np.array( [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0]] ) 

k = min_k_for_Bk(A)
print(f"diameter: {k}")


G_specific = nx.DiGraph()
G_specific.add_nodes_from(range(7))

for i in range(7):
    for j in range(7):
        if A[i][j] == 1:
            G_specific.add_edge(i, j)

plt.figure(figsize=(8, 6))
nx.draw(G_specific, with_labels=True, node_color='lightgreen', node_size=700, arrowstyle='-|>', arrowsize=20)
plt.title('示意图：特定的7个节点的有向图')
plt.show()
