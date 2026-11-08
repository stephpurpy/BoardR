from board.board import Board
from board.can_add_item import CanAddItem

class ReadonlyBoard(Board, CanAddItem):
    pass