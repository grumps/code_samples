__author__ = 'DanielPearl, MaxResnick'
__all__ = ['']
from Connect4.c4_controller import C4Controller


class Connect4:
    """
    used to run connect4.
    """
    def __init__(self):
        new_game = C4Controller()
        new_game.main()


if __name__ == "__main__":
    run_game = Connect4()
