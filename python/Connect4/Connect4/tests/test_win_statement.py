__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from io import StringIO

from c4_view import C4View

class WinngStatementTest(unittest.TestCase):
    """ Tests if winning statement is printed."""
    # TODO add error messages.

    def setUp(self):
        self.test_view = C4View()
        print(self.shortDescription())

    @patch('sys.stdout', new_callable=StringIO)
    def test_winning_statement_print(self, mock_stdout):
        """test if a tie statement is printed correctly."""
        winning_statement = \
            ("Congrats {} you've won!!!!\n").format("Bob")
        self.test_view.win_statement("Bob")
        self.assertEqual(winning_statement, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
