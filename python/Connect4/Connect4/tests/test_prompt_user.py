__author__ = 'DanielPearl'

import unittest
from c4_view import C4View
from unittest.mock import patch
from io import StringIO

class PromptTurnTest(unittest.TestCase):
    """Test turn prompt"""

    # TODO add custom error messages.

    def setUp(self):
        self.test_view = C4View()
        print(self.shortDescription())

    @patch ('builtins.input', return_value='1')
    def test_valid_single_input(self, return_value):
        """prompt is given a single input, returns single char string"""
        self.assertEqual("1",self.test_view.prompt_turn("Bob"))

    @patch ('builtins.input', return_value='12')
    def test_valid_multiple_input(self, return_value):
        """prompt is given a multiple input, returns single char string"""
        self.assertEqual("12",self.test_view.prompt_turn("Bob"))


if __name__ == '__main__':
    unittest.main()
