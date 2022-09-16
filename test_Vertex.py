import unittest
from Vertex import Vertex


class TestVertex(unittest.TestCase):
    def test_attempt_to_initiate_an_empty_Vertex_instance(self):
        with self.assertRaises(TypeError):
            _ = Vertex()

    def test_attempt_to_initiate_a_new_Vertex_instance(self):
        _ = Vertex(1)

    def test_attempt_to_add_new_neighbor_to_a_Vertex(self):
        self.assertTrue(Vertex(1).new_neighbor(Vertex(2), 3))

    def test_attempt_to_add_new_neighbor_with_non_Vortex_argument(self):
        with self.assertRaises(TypeError):
            _ = Vertex(1).new_neighbor(2, 3)

    def test_attempt_to_add_new_neighbor_with_non_integer_distance_argument(self):
        with self.assertRaises(TypeError):
            _ = Vertex(1).new_neighbor(Vertex(2), 3.2)

    def test_if_neighbor_is_listed(self):
        main = Vertex(1)
        test = Vertex(2)
        main.new_neighbor(test, 4)
        self.assertTrue(main.has_neighbor(test))


if __name__ == '__main__':
    unittest.main()
