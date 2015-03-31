import sys
from json import dumps
from collections import Counter

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

def print_jsonify_error(error):
    formatted_error = dumps([{"message":error}],
                                 indent=4, 
                                 separators=(',',':'))
    print formatted_error
    sys.argv.append(formatted_error)
    sys.exit(1)

def print_jsonify_output(output):
    json_output = []

    for game_state in output:
        json_game_state = {"indexes":game_state}
        json_output.append(json_game_state)

    formatted_output = dumps(json_output, 
                                    indent=4, 
                                    separators=(',',':'))
    print formatted_output
    sys.exit(0)

## VALIDATORS

def validate_input_board(board):
    message = None

    if board and len(board) < 9:
        message = "Board is too small."

    elif board and len(board) > 9:
        message = "Board is too large."

    if not board or board == "None":
        message = "Invalid board -- no board passed in."

    if message: print_jsonify_error(message)

    return None

def validate_board(board, lines):

    message = None

    def is_invalid_length():
        return len(board) is not 9

    def is_at_end_state():
        for line in lines:
            if line.is_end_state():
                return True
        return False

    if is_at_end_state():
        message = "Board at end state."

    if is_invalid_length():
        message = "Incorrect number of cells."

    if message: print_jsonify_error(message)

    return None

def validate_player(player):

    message = None

    if player.state not in ['x', 'o']:
        message = "Invalid player -- choose x or o."

    if not player.state:
        message = "Invalid player -- please pass in a player."

    if message: print_jsonify_error(message)

    return None


def validate_cell(cell):
    if cell.state not in ['*', 'x', 'o']:
        message = "Invalid cell state for cell {0}.".format(cell.id)
        print_jsonify_error(message)

    if cell.id < 0 or cell.id > 8:
        message = "Invalid cell id {0}.".format(cell.id)
        print_jsonify_error(message)
