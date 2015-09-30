__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from c4_view import C4View


class PromptNameTest(unittest.TestCase):
    """Test turn prompt name"""

    # TODO add custom error messages.

    def setUp(self):
        self.test_view = C4View()
        print(self.shortDescription())

    @patch ('builtins.input', return_value='Mr. Smith')
    def test_valid_single_input(self, return_value):
        """prompt is given a single input, returns single char string"""
        self.assertEqual("Mr. Smith",self.test_view.prompt_name(1))

if __name__ == '__main__':
    unittest.main()
