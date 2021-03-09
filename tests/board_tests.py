import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'gameoflife')))

from board import Board

class TestBoard(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.B = Board(width=3, height=3)


    def test_board_setup(self):
        self.assertEqual(self.B.width, 3)
        self.assertEqual(self.B.height, 3)
        self.assertEqual(self.B.generation, 0)


    def test_board_created(self):
        self.assertNotEqual(self.B.board, None)
        for row in self.B.board:
            for cell in row:
                self.assertEqual(cell.state, 0)


    def test_neighbour_setup(self):
        """Tests all that all cells in the board have the approrpiate amount of
        neighbours"""
        corner_cells = [self.B.board[0][0], self.B.board[0][2],
                        self.B.board[2][0], self.B.board[2][2] ]
        edge_cells = [self.B.board[0][1], self.B.board[2][1],
                        self.B.board[1][0], self.B.board[1][2] ]


        for cell in corner_cells:
            self.assertEqual(len(cell.neighbours), 3)

        for cell in edge_cells:
            self.assertEqual(len(cell.neighbours), 5)

        self.assertEqual(len(self.B.board[1][1].neighbours), 8)


    def test_dead_state(self):
        self.B.board[0][0].state, self.B.board[0][0].prev_state = 1, 1
        self.B.generation = 3

        not_dead = True
        for row in self.B.board:
            for cell in row:
                if cell.state == 1:
                    not_dead = False

        self.assertEqual(not_dead, False)
        self.assertEqual(self.B.generation, 3)

        self.B.dead_state()
        for row in self.B.board:
            for cell in row:
                self.assertEqual(cell.state, 0)
                self.assertEqual(cell.prev_state,0)

        self.assertEqual(self.B.generation, 0)


    def test_next_state(self):
        self.B.board[1][0].state, self.B.board[1][0].prev_state,\
        self.B.board[1][1].state, self.B.board[1][1].prev_state,\
        self.B.board[1][2].state, self.B.board[1][2].prev_state = 1,1,1,1,1,1

        cell_state1 = [0,0,0,
                       1,1,1,
                       0,0,0]
        #Get current state of the board
        cell_current_state = []
        cell_current_prev_state = []
        for row in self.B.board:
            for cell in row:
                cell_current_state.append(cell.state)
                cell_current_prev_state.append(cell.prev_state)
        #Assert that all our set up is what it should be.
        self.assertEqual(cell_current_state, cell_state1)
        self.assertEqual(cell_current_prev_state, cell_state1)
        self.assertEqual(self.B.generation, 0)


        self.B.next_state()
        cell_state2 = [0,1,0,
                       0,1,0,
                       0,1,0]
        cell_current_state = []
        cell_current_prev_state = []
        #get what the state of teh board is after the change
        for row in self.B.board:
            for cell in row:
                cell_current_state.append(cell.state)
                cell_current_prev_state.append(cell.prev_state)
        #assert that the change worked properly
        self.assertEqual(cell_current_state, cell_state2)
        self.assertEqual(cell_current_prev_state, cell_state2)
        self.assertEqual(self.B.generation, 1)


    def test_load_file(self):
        exploder = self.B._load_file("explodersmall.txt")
        expected = [[0,1,0],
                    [1,1,1],
                    [1,0,1],
                    [0,1,0]]
        self.assertEqual(exploder, expected)


    def test_load_state(self):
        B = Board(3,4)
        B.load_state("explodersmall.txt")

        state=[]

        for row in B.board:
            for cell in row:
                state.append(cell.state)

        expected = [0,1,0,
                    1,1,1,
                    1,0,1,
                    0,1,0]
        self.assertEqual(state, expected)


    def test__apply_state(self):
        B = Board(3,3)
        states = [[1,1,1],[1,1,1],[1,1,1]]
        B._apply_state(states)
        test = False
        for row in B.board:
            for cell in row:
                if cell.state == 0:
                    test = True

        self.assertEqual(test, False)






if __name__ == "__main__":
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
