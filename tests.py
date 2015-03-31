import unittest
from json import dumps
import sys
from tic_tac_toe import main

class TestValidTicTacToeAI(unittest.TestCase):

    def setUp(self):
        self.old_sys_argv = sys.argv
        self._input = dumps([
                        {
                            "board":"****x****",
                            "player": "o"
                        },
                        {
                            "board":"o***xo*x*",
                            "player": "o"
                        },
                        {
                            "board":"*oo*xx***",
                            "player": "x"
                        }
                    ])
        sys.argv = ['', self._input]
  
    def tearDown(self):
        sys.argv = self.old_sys_argv
        self._input = None

    def test_systemExit0(self):

        try:
            main()
        except SystemExit as e:
            self.assertEqual(e.message, 0)

    def test_stdoutputMatches(self):

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(),
                            dumps([{"indexes": [8, 6, 2, 0, 7, 5, 3, 1]}, 
                                    {"indexes": [1, 2, 6, 8, 3]}, 
                                    {"indexes": [3, 0, 8, 6, 7]}], 
                                    indent=4, separators=(',',':')
                                )
                            )

class TestInvalidTicTacToeAI(unittest.TestCase):

    def setUp(self):
        self.old_sys_argv = sys.argv

    def tearDown(self):
        sys.argv = self.old_sys_argv
        self._input = None

    def test_invalid_board_too_few_cells(self):
        self._input = dumps([
                                {
                                    "board":"**oox*",
                                    "player": "o"
                                }
                            ])
        sys.argv = ['', self._input]

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(), 
                            dumps([{"message": "Board is too small."}], 
                                    indent=4, separators=(',',':'))
                                )

    def test_invalid_board_too_many_cells(self):
        self._input = dumps([
                                {
                                    "board":"**ooxxxooooxxx**xo",
                                    "player": "o"
                                }
                            ])
        sys.argv = ['', self._input]

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(), 
                            dumps([{"message": "Board is too large."}], 
                                    indent=4, separators=(',',':'))
                                )

    def test_invalid_board_wrong_cell_type(self):
        self._input = dumps([
                        {
                            "board":"*?**x**o*",
                            "player": "o"
                        }
                    ])
        sys.argv = ['', self._input]

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(), 
                            dumps([{"message": "Invalid cell state for cell 1."}], 
                                    indent=4, separators=(',',':'))
                                )

    def test_invalid_board_not_passed_in(self):
        self._input = dumps([
                        {
                            "player": "o"
                        }
                    ])
        sys.argv = ['', self._input]

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(), 
                            dumps([{"message": "Invalid board -- no board passed in."}], 
                                    indent=4, separators=(',',':'))
                                )

    def test_board_at_end_state(self):
        self._input = dumps([
                        {
                            "board":"xxxooxo**",
                            "player": "o"
                        }
                    ])
        sys.argv = ['', self._input]

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(), 
                            dumps([{"message": "Board at end state."}], 
                                    indent=4, separators=(',',':'))
                                )

    def test_invalid_player_not_passed_in(self):
        self._input = dumps([
                        {
                            "board":"xx**oxo**"
                        }
                    ])
        sys.argv = ['', self._input]

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(), 
                            dumps([{"message": "Invalid player -- please pass in a player."}], 
                                    indent=4, separators=(',',':'))
                                )

    def test_invalid_player_wrong_player_type(self):
        self._input = dumps([
                        {
                            "board":"xx**oxo**",
                            "player":"?"
                        }
                    ])
        sys.argv = ['', self._input]

        try:
            main()
        except SystemExit as e:
            self.assertEqual(sys.stdout.getvalue().strip(), 
                            dumps([{"message": "Invalid player -- choose x or o."}], 
                                    indent=4, separators=(',',':'))
                            )

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=True)

