__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from io import StringIO

from c4_view import C4View

class TieStatementTest(unittest.TestCase):
    """ Tests if winning statement is printed."""
    # TODO add error messages.

    def setUp(self):
        self.test_view = C4View()
        print(self.shortDescription())

    @patch('sys.stdout', new_callable=StringIO)
    def test_tie_statement_print(self, mock_stdout):
        """test if a winning statement is printed correctly."""
        tie_statement = \
            ("The board is full, no one wins X_x,"
             "basically you're both losers.\n")
        self.test_view.tie_statement()
        self.assertEqual(tie_statement, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
