import sys
from json import loads
from helpers import print_jsonify_output, print_jsonify_error, byteify
from models import Board, Player


def main():
    _input = sys.argv[1]

    try:
        game_states = byteify(loads(_input))

    except (SyntaxError, TypeError) as e:
        print_jsonify_error("Input was not properly formed JSON.")

    output = []

    for game_state in game_states:

        board = Board(game_state.get("board"))
        player = Player(game_state.get("player"))

        ranked_moves = board.rank_moves(player)
        output.append(ranked_moves)

    print_jsonify_output(output)

if __name__ == "__main__":
    main()

