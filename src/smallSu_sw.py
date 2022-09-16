import numpy as np
import pyswarms

from Graph import Graph
from Graph.Vertex import Vertex

v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)

v0.new_neighbor(v1, 4)
v1.new_neighbor(v0, 4).new_neighbor(v2, 1).new_neighbor(v3, 3).new_neighbor(v4, 7)
v2.new_neighbor(v1, 1).new_neighbor(v3, 2).new_neighbor(v4, 3)
v3.new_neighbor(v1, 3).new_neighbor(v2, 2)
v4.new_neighbor(v1, 7).new_neighbor(v2, 3)

list_of_vertices = [v0, v1, v2, v3, v4]

graph = Graph(list_of_vertices)
vertices = graph.keys


def fitness(the_solution):
    predecessor = 0
    check_list = vertices.copy()
    result = 0

    for each in the_solution:
        if each in graph.get_value(predecessor):  # If each is a neighbour
            result -= graph.get_value(predecessor)[each]  # Go

            if each in check_list:  # If it is a first visit => check
                check_list.remove(each)

            if each == 0:  # If returned to 0
                if len(check_list) == 0:  # If visited every vertex
                    return result  # OK
                return -999  # Finished to early

            predecessor = each
        elif each == predecessor:  # If each doesn't move
            continue
        else:
            return -999  # Attempt to jump over path!

    if len(check_list) == 0:
        return result

    return result - 500


def f(x):
    n_particles = x.shape[0]
    j = [-1 * fitness(x[i]) for i in range(n_particles)]
    return np.array(j)


options = {
    'c1': 0.5,
    'c2': 0.3,
    'w': 0.9
}

max_bound = 4 * np.ones(8)
min_bound = np.zeros(8)
bounds = (min_bound, max_bound)

optimizer = pyswarms.single.GlobalBestPSO(
    n_particles=10,
    dimensions=8,
    options=options,
    bounds=bounds,
    init_pos=np.zeros(8)
)

cost, pos = optimizer.optimize(f, iters=1000)
