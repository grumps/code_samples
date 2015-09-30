__author__ = 'DanielPearl'

import unittest
from c4_controller import C4Controller


class UpdateBoardTest(unittest.TestCase):
    def setUp(self):
        self.controller = C4Controller()
        print(self.shortDescription())

    def test_does_board_update(self):
        """tests if update if valid"""
        expected = (1, 1)
        actual = self.controller.update_board(1)
        self.assertEqual(expected, actual)

    def test_does_board_not_update(self):
        """tests if update if non valid column"""
        expected = (None, None)
        actual = self.controller.update_board(8)
        self.assertEqual(expected, actual)

    def test_does_board_not_update_give_bad_type(self):
        """tests if given non-valid column type"""
        expected = (None, None)
        actual = self.controller.update_board("8")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
