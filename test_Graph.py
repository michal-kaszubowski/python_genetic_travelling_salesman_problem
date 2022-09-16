import unittest
from Vertex import Vertex as Vertex
from Graph import Graph as Graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Vertex(1)
        self.b = Vertex(2)
        self.c = Vertex(3)
        self.d = Vertex(4)

    def test_attempt_to_make_empty_graph(self):
        with self.assertRaises(TypeError):
            _ = Graph()

    def test_attempt_to_make_new_dot_graph(self):
        _ = Graph([self.a, self.b, self.c, self.d])

    def test_invalid_list_of_vertices(self):
        with self.assertRaises(TypeError):
            _ = Graph([self.a, 2, self.c, self.d])

    def test_graph_keys(self):
        graph = Graph([self.a, self.b, self.c, self.d])
        self.assertEqual(graph.keys, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
