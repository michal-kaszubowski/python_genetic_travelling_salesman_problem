class Vertex:
    def __init__(self, name):
        self.__name = name
        self.__neighbors = {}

    def __eq__(self, other):
        return isinstance(other, Vertex)  # Why I can not use "==" operator in new_neighbor !!??

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not int:
            raise TypeError("Invalid type!")
        self.__name = name

    def new_neighbor(self, vertex, distance):
        if not isinstance(vertex, Vertex):
            raise TypeError("Has to be a proper instance of Vertex!")
        if not isinstance(distance, int):
            raise TypeError("Distance is not an integer!")

        if vertex.name in self.__neighbors:
            raise Exception("Already listed!")
        self.__neighbors[vertex.name] = distance
        return self

    def has_neighbor(self, other_vertex):
        return other_vertex.name in self.__neighbors

    @property
    def neighbors(self):
        return self.__neighbors
