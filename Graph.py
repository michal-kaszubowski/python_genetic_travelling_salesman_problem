from Vertex import Vertex


class Graph:
    def __init__(self, list_of_vertices):
        # We can assume that graph cannot be empty so a list of some kind have to be given
        if not isinstance(list_of_vertices, list):
            raise TypeError("Inappropriate argument supported. Is not a list!")

        self.__vertices = {}
        for each in list_of_vertices:
            if not isinstance(each, Vertex):
                raise TypeError("Error while parsing argument. One of the object is not an instance of Vertex!")
            self.__vertices[each.name] = each.neighbors

    @property
    def vertices(self):
        return self.__vertices

    @property
    def keys(self):
        return list(self.__vertices.keys())

    def get_value(self, key):
        return self.__vertices[key]
