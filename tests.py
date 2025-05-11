import unittest
from maze import *


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        
    
    def test_entrance_and_exit_creation(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        col, row = 0, 0
        self.assertFalse(m1._cells[col][row].has_top_wall)

        col, row = len(m1._cells) - 1, len(m1._cells[0]) - 1
        self.assertFalse(m1._cells[col][row].has_bottom_wall)


if __name__ == "__main__":
    unittest.main()