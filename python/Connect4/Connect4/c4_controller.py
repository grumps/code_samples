__author__ = 'DanielPearl, MaxResnick'
from c4_model import C4Model
from c4_view import C4View


class C4Controller:
    """
    Connect 4 controller
    """

    def __init__(self):
        self.model = C4Model()
        self.view = C4View()

    def update_board(self, col_num):
        """
        :param col_num: column number int
        """
        if type(col_num) == int and col_num < 8 and col_num > 0:
            return self.model.add_piece(col_num)
        else:
            return (None, None)

    def check_winner(self, col_num, row_num):
        """
        :param board: board list
        :return: winning player
        """
        horiz = "".join(self.model.get_column(col_num))
        vert = "".join(self.model.get_row(row_num))
        temp1, temp2 = self.model.get_diagonal(col_num, row_num)
        diag_pos = "".join(temp1)
        diag_neg = "".join(temp2)

        player1_win = self.model.PLAYER_1_PIECE * 4
        player2_win = self.model.PLAYER_2_PIECE * 4

        if player1_win in horiz or player1_win in vert or player1_win in diag_pos or player1_win in diag_neg:
            return True
        elif player2_win in horiz or player2_win in vert or player2_win in diag_pos or player2_win in diag_neg:
            return True
        else:
            return False

    def check_tie(self):
        """
        :print: no more moves, players tie
        """
        for column in self.model.board:
            if "-" in column:
                return False
        return True

    def get_player_names(self):
        """
        gets player name and sets player
        """
        player1 = ""
        player2 = ""
        player_names_valid = False
        while not player_names_valid:
            if player1 == "":
                player1 = self.view.prompt_name(1)

            if player2 == "":
                player2 = self.view.prompt_name(2)

            if len(player1) > 0 and len(player2) > 0:
                player_names_valid = True

        self.model.set_player(player1)
        self.model.set_player(player2)

    def turn_validator(self, col_num):
        """
        :param dirty_input: raw input from user
        :return: number of column
        """
        if len(col_num) == 1 and col_num.isnumeric():
            int_col = int(col_num)
            if "-" in self.model.get_column(int_col) and int_col < 8:
                return True

        return False

    def main(self):
        self.view.show_instructions()
        self.get_player_names()

        gameover = False
        while not gameover:
            self.view.print_board(self.model.board)
            current_player = self.model.get_player(self.model.current_turn)
            user_input = self.view.prompt_turn(current_player)
            if self.turn_validator(user_input):
                col, row = self.update_board(int(user_input))
                if self.check_winner(col, row):
                    self.view.print_board(self.model.board)
                    self.view.win_statement(current_player)
                    gameover = True
                elif self.check_tie():
                    self.view.print_board(self.model.board)
                    self.view.tie_statement()
                    gameover = True
            self.model.update_turn()

if __name__ == '__main__':
    new_game = C4Controller()

