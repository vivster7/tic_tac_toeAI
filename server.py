import sys
from flask import Flask, request, make_response
from json import dumps
from models import Player, Board
app = Flask(__name__)

@app.route("/next-move")
def next_move():

    player = str(request.args.get("player"))
    board = str(request.args.get("board"))

    try:

        player = Player(player)
        board = Board(board)

        ranked_moves = board.rank_moves(player)

    except SystemExit as e:
        error = sys.argv[-1]
        response = make_response(error, 400)
        response.headers['Content-Type'] = "application/json"
        return response

    response = make_response(dumps([{"indexes":ranked_moves}],
                                     indent=4, separators=(',',':')))
    response.headers['Content-Type'] = "application/json"
    return response

if __name__ == "__main__":
    app.run()