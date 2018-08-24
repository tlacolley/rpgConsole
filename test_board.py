#!/usr/bin/env python
# -- coding: UTF-8 --
from core.board import Board
from core.character import Wizard
import unittest

class TestBoard(unittest.TestCase):

    def testBoardInitialisation(self):
        board = Board(50, 50)
        self.assertTrue(len(board.grid) == 50)
        for lig in range(50):
            self.assertTrue(len(board.grid[lig]) == 50)
            for col in range(50):
                cell = board.grid[lig][col]
                self.assertListEqual(cell, [])

    def testCharacterMove(self):
        board = Board(50, 50)
        w = Wizard("Plop")
        self.assertEqual(w.x, None)
        self.assertEqual(w.y, None)

        board.move(w, 0, 0)
        self.assertEqual(w.x, 0)
        self.assertEqual(w.y, 0)
        cell = board.grid[0][0]
        self.assertTrue(w in cell)

        cell_before_move = board.grid[w.x][w.y]
        board.move(w, 2, 4)
        self.assertEqual(w.x, 2)
        self.assertEqual(w.y, 4)
        cell = board.grid[2][4]
        self.assertTrue(w not in cell_before_move)
        self.assertTrue(w in cell)

    def testDisplay(self):
        board = Board(20, 20)

        expected_display = "--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n"
        self.assertEqual(board.display(), expected_display)

        w = Wizard("Plop")
        board.move(w, 0, 0)
        expected_display = "X-------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n"
        self.assertEqual(board.display(), expected_display)

        board.move(w, 2, 4)
        expected_display = "--------------------\n--------------------\n----X---------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n--------------------\n"
        self.assertEqual(board.display(), expected_display)


if __name__ == '__main__':
    unittest.main()
