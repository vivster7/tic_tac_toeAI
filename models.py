from collections import Counter
from helpers import validate_board, validate_player, validate_cell, validate_input_board

class Player(object):
    def __init__(self, state):
        self._state = state

        validate_player(self)

    @property
    def state(self):
        return self._state


class Board(object):
    def __init__(self, board):

        validate_input_board(board)

        cells = Board.init_cells(board)
        lines = Board.init_lines(cells)

        self._board = cells
        self._lines = lines

        validate_board(self._board, self._lines)

    @property
    def board(self):
        return self._board

    @property
    def lines(self):
        return self._lines
    

    def rank_moves(self, player):

        cells = []

        for cell in self.board:

            if cell.state is Cell.NEUTRAL_STATE:
                cell.update_points_from_move(player)
                cells.append(cell)

        cells.sort(key = lambda cell: (cell.points, cell.id), reverse=True)

        indexes = map(lambda cell: cell.id, cells)

        return indexes

    @staticmethod
    def init_cells(board):

        cells = []

        for index,elem in enumerate(board):

            cell = Cell(index, elem)
            validate_cell(cell)

            cells.append(cell)

        return cells

    @staticmethod
    def init_lines(cells):

        # Horizontal Lines
        line1 = Line(1,[cells[0], cells[1], cells[2]])
        line2 = Line(2,[cells[3], cells[4], cells[5]])
        line3 = Line(3,[cells[6], cells[7], cells[8]])

        # Vertical Lines
        line4 = Line(4,[cells[0], cells[3], cells[6]])
        line5 = Line(5,[cells[1], cells[4], cells[7]])
        line6 = Line(6,[cells[2], cells[5], cells[8]])

        # Diagonal Lines
        line7 = Line(7,[cells[0], cells[4], cells[8]])
        line8 = Line(8,[cells[2], cells[4], cells[6]])

        lines = [line1, line2, line3, line4, line5, line6, line7, line8]

        return lines


class Cell(object):

    NEUTRAL_STATE = "*"
    X_STATE = "x"
    O_STATE = "o"

    def __init__(self, id, state, points=0):
        self._id = id
        self._state = state
        self._points = points
        self._lines = set()

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def lines(self):
        return self._lines
        
    @lines.setter
    def lines(self, value):
        self._lines = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    def update_points_from_move(self, player):

        points = 0

        for line in self.lines:
            points += line.points_from_move(player)

        self.points = points

        return None

class Line(object):
    """ A Line consists of three cells that can be used to win a TicTacToe game."""

    def __init__(self,id, cells):
        self._id = id
        self._cells = cells

        self.update_cells(self._cells)

    @property
    def id(self):
        return self._id

    @property
    def cells(self):
        return self._cells

    def update_cells(self, cells):
        for cell in cells:
            cell.lines.add(self)

    def points_from_move(self, player):

        cell_states = map(lambda cell: cell.state, self.cells)
        line_state = Counter(cell_states)
        points = self.points_from_line_state(line_state, player)
        return points


    def points_from_line_state(self, line_state, player):

        if player.state == 'x':

            if line_state == Counter(['*','x','o']): return 0
            if line_state == Counter(['*','*','*']): return 1
            if line_state == Counter(['*','*','o']): return 5
            if line_state == Counter(['*','*','x']): return 25
            if line_state == Counter(['*','o','o']): return 125
            if line_state == Counter(['*','x','x']): return 625

        if player.state == 'o':

            if line_state == Counter(['*','x','o']): return 0
            if line_state == Counter(['*','*','*']): return 1
            if line_state == Counter(['*','*','x']): return 5
            if line_state == Counter(['*','*','o']): return 25
            if line_state == Counter(['*','x','x']): return 125
            if line_state == Counter(['*','o','o']): return 625

    def is_end_state(self):

        cell_states = map(lambda cell: cell.state, self.cells)
        line_state = Counter(cell_states)

        if line_state == Counter(['x','x','x']): return True
        if line_state == Counter(['o','o','o']): return True

        return False
