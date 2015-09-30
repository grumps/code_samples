__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from c4_controller import C4Controller

class TurnValidatorTest(unittest.TestCase):
    def setUp(self):
        self.controller = C4Controller()
        print(self.shortDescription())
        self.controller.model.board = [['X', 'X', 'X', 'X', 'X', 'X'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-']]

    def test_valid_turn(self):
        """given a single input string, expect that to be returned as an int"""
        actual = self.controller.turn_validator("2")
        self.assertTrue(actual)

    def test_invalid_turn(self):
        """given a single input string, expect that to be returned as True"""
        actual = self.controller.turn_validator("1")
        self.assertFalse(actual)

    def test_too_many_columns_turn(self):
        """given a column that doesn't exist, expect that to be returned False"""
        actual = self.controller.turn_validator("8")
        self.assertFalse(actual)

    def test_more_than_one_turn(self):
        """given multiple input strings, expect that to be returned as False"""
        actual = self.controller.turn_validator("2t")
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
