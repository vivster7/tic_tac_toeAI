import sys
import helpers
from json import loads, dumps
from models import Board, Player

def main():
    _input = sys.argv[1]

    try:
        game_states = helpers.byteify(loads(_input))

    except (ValueError) as e:
        print "Invalid JSON input"
        helpers.error_occurred = True
        return None

    output = []

    for game_state in game_states:

        try:

            board = Board(game_state.get("board"))
            player = Player(game_state.get("player"))

            ranked_moves = board.rank_moves(player)
            output.append({"indexes":ranked_moves})

        except ValueError as e:

            output.append({"message":e.message})
            helpers.error_occurred = True

    json_output = dumps(output, indent=4, separators=(',',':'))

    print json_output
    return json_output

if __name__ == "__main__":
    main()

    if helpers.error_occurred: 
        sys.exit(1)

    sys.exit(0)

