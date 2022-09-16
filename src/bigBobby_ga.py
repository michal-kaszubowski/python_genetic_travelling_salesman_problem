import pygad

from Graph import Graph
from Vertex import Vertex

v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)

v0.new_neighbor(v1, 3).new_neighbor(v2, 1).new_neighbor(v5, 4)
v1.new_neighbor(v0, 3).new_neighbor(v2, 2).new_neighbor(v4, 3)
v2.new_neighbor(v0, 1).new_neighbor(v1, 2).new_neighbor(v3, 2)
v3.new_neighbor(v2, 2).new_neighbor(v4, 3).new_neighbor(v5, 7).new_neighbor(v7, 2)
v4.new_neighbor(v1, 3).new_neighbor(v3, 3).new_neighbor(v5, 4).new_neighbor(v6, 3)
v5.new_neighbor(v0, 4).new_neighbor(v3, 7).new_neighbor(v4, 4).new_neighbor(v6, 2).new_neighbor(v7, 6)
v6.new_neighbor(v4, 3).new_neighbor(v5, 2).new_neighbor(v7, 7)
v7.new_neighbor(v3, 2).new_neighbor(v5, 6).new_neighbor(v6, 7)

list_of_vertices = [v0, v1, v2, v3, v4, v5, v6, v7]

graph = Graph(list_of_vertices)
vertices = graph.keys
gene_space = [0, 1, 2, 3, 4, 5, 6, 7]


def drakken(the_solution, the_solution_idx):
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
    # Side note. Draconian version of this function cause that most of the time problem is not solved!


def good_cop(the_solution, the_solution_idx):
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
                result -= 500  # Finished to early

            predecessor = each
        elif each == predecessor:  # If each doesn't move
            continue
        else:
            result -= 100  # Attempt to jump over path!

    if len(check_list) == 0:
        return result

    return result - 500
    # Side note. Draconian version of this function cause that most of the time problem is not solved!


# =============================

fitness_function = good_cop

sol_per_pop = 100
num_genes = len(vertices) * 2

num_parents_mating = 50
num_generations = 1000
keep_parents = 10

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 50

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

ga_instance.plot_fitness()
