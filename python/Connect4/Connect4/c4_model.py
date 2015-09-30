__author__ = 'DanielPearl, MaxResnick'


class C4Model:

    """Connect 4 model"""

    # Model constants.
    PLAYER_1_PIECE = "\033[94m☻\033[0m"
    PLAYER_2_PIECE = "\033[92m☻\033[0m"

    def __init__(self):
        self.board = self.make_board()
        self.players = []
        self.current_turn = 1

    def make_board(self):
        """
        Creates empty board
        :return: 2D array
        """
        board = []
        for row in range(7):
            board.append(["-"]*6)
        return board

    def get_player(self, player_postion):
        """
        :param player_postion: position of player
        :return: player str
        """
        return self.players[player_postion-1]

    def set_player(self, name):
        """
        :param name: Player name
        :return: player name
        """
        self.players.append(name)
        return self.players

    def update_turn(self):
        """
        :return: player's turn
        """
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1

        return self.current_turn

    def get_column(self, col_num):
        """
        Given column, return row
        :param col_num: column number as int
        :return: list of pieces
        """
        if (len(self.board) < col_num) or (col_num == 0):
            return []
        return self.board[col_num-1]

    def get_row(self, row_num):
        """
        Given row, return column
        :param row_num: row number as int
        :return: dictionary
        """

        row = []
        for col_index, col in enumerate(self.board):
            if len(self.board[col_index]) < row_num:
                return None
            row.append(self.board[col_index][row_num-1])
        return row

    def get_diagonal(self, col, row):
        """
        Gets two diagonal lists from a given position of a piece
        :param col: column as integer, not  index
        :param row: row as integer, not index
        :return: [diagonal], [diagonal^1]
        """
        diagonal = []
        diagonal2 = []
        # We're utilzing y = mx + b to linearly traverse the data structure.
        const = (row-1) - (col-1)
        for column_index, column in enumerate(self.board):
            target_row_position = column_index + const
            if target_row_position <= 5 and target_row_position >= 0:
                diagonal.append(self.board[column_index][target_row_position])
        # Go the opposite direction i.e. inverse function.
        const_2 = (row-1) + (col-1)
        for column_index, column in enumerate(self.board):
            target_row_position_2 = -1 * column_index + const_2
            if target_row_position_2 <= 5 and target_row_position_2 >= 0:
                diagonal2.append(self.board[column_index][target_row_position_2])
        return (diagonal, diagonal2)


    def add_piece(self, col_num):
        """
        :param col_num: column int
        :param player: player
        :return: True, False & indexes of position (col, row)
        """
        if self.current_turn == 1:
            piece = self.PLAYER_1_PIECE
        else:
            piece = self.PLAYER_2_PIECE
        col_index = col_num - 1

        if "-" in self.board[col_index]:
            row_index = self.board[col_index].index("-")
            self.board[col_index][row_index] = piece
            return (col_index + 1, row_index + 1)
        else:
            return (None,None)

if __name__ == '__main__':
    new = C4Model()
