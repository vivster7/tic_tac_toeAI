import sys
from json import dumps
from collections import Counter

## Error indicator
error_occurred = False

## FORMATTING

def byteify(input):
    """ Transforms unicode output from json.loads() to utf-8. """

    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key, value in input.iteritems()}

    elif isinstance(input, list):
        return [byteify(element) for element in input]

    elif isinstance(input, unicode):
        return input.encode('utf-8')

    else:
        return input

## VALIDATORS

def validate_input_board(board):

    error_message = ''

    if board and len(board) < 9:
        error_message = "Board is too small."

    elif board and len(board) > 9:
        error_message = "Board is too large."

    if not board or board == "None":
        error_message = "Invalid board -- no board passed in."

    if error_message: raise ValueError(error_message)

    return None

def validate_board(board, lines):

    error_message = ''

    def is_invalid_length():
        return len(board) is not 9

    def is_at_end_state():
        for line in lines:
            if line.is_end_state():
                return True
        return False

    if is_at_end_state():
        error_message = "Board at end state."

    if is_invalid_length():
        error_message = "Incorrect number of cells."

    if error_message: raise ValueError(error_message)

    return None

def validate_player(player):

    error_message = ''

    if player.state not in ['x', 'o'] or len(player.state) != 1:
        error_message = "Invalid player -- choose x or o."

    if not player.state:
        error_message = "Invalid player -- please pass in a player."

    if error_message: raise ValueError(error_message)

    return None


def validate_cell(cell):

    error_message = ''

    if cell.state not in ['*', 'x', 'o']:
        error_message = "Invalid cell state for cell {0}.".format(cell.id)

    if cell.id < 0 or cell.id > 8:
        error_message = "Invalid cell id {0}.".format(cell.id)
        
    if error_message: raise ValueError(error_message)

    return None