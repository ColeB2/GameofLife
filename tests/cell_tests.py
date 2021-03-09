import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'gameoflife')))

from cell import Cell

class TestCell(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Basic Cell class setup. Creating a mini 4 cell neighbourhood, and
        calling the get_neighbours class to set up neighbours on all cells.
        Doesn't call get_neighbours on C4, as to save it for a later test."""
        self.C1 = Cell(0,0, state=0)
        self.C2 = Cell(1,0, state=0)
        self.C3 = Cell(0,1, state=0)
        self.C4 = Cell(1,1, state=1)
        self.Board = [[self.C1, self.C2],
                      [self.C3, self.C4]]
                      
        self.C1.get_neighbours(self.Board)
        self.C2.get_neighbours(self.Board)
        self.C3.get_neighbours(self.Board)

    def test_proper_setup(self):
        self.assertEqual(self.C1.x, 0)
        self.assertEqual(self.C1.y, 0)
        self.assertEqual(self.C1.state, 0)
        self.assertEqual(self.C1.prev_state, self.C1.state)
        self.assertEqual(len(self.C1.neighbours), 3)

    def test_get_neighbours(self):
        cell_1_neighbours = [self.C2, self.C3, self.C4]
        for i in range(len(self.C1.neighbours)):
            self.assertEqual(self.C1.neighbours[i], cell_1_neighbours[i])

        cell_2_neighbours = [self.C1, self.C3, self.C4]
        for i in range(len(self.C2.neighbours)):
            self.assertEqual(self.C2.neighbours[i], cell_2_neighbours[i])

        cell_3_neighbours = [self.C1, self.C2, self.C4]
        for i in range(len(self.C3.neighbours)):
            self.assertEqual(self.C3.neighbours[i], cell_3_neighbours[i])


    def test_check_neighbour_state(self):
        self.C1.check_neighbour_state()
        self.assertEqual(self.C1.alive_neighbours, 1)

    def test_draw_state(self):
        C=Cell(0,0,state=0)
        self.assertEqual(C.state,0)
        C.draw_state()
        self.assertEqual(C.state,1)

    def test_calculate_state(self):
        self.C4.get_neighbours(self.Board)

        cell_4_neighbours = [self.C1, self.C2, self.C3]
        for i in range(len(self.C4.neighbours)):
            self.assertEqual(self.C4.neighbours[i], cell_4_neighbours[i])
        self.assertEqual(self.C4.state, 1)

        self.C4.check_neighbour_state()
        self.assertEqual(self.C4.alive_neighbours, 0)

        self.C4.calculate_state()
        self.assertEqual(self.C4.state, 0)





if __name__ == "__main__":
    unittest.main()
