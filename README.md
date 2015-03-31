## Basic version

Basic tic-tac-toe AI implementation. Given an input (stdin) of a board and a player, the AI returns the order of each possible move ranked from best to worst.

You can run a commond line tic-tac-toe AI with the command

```bash
    $ python tic_tac_toe.py JSON_INPUT
    
    #For example:
    $ python tic_tac_toe.py '[{ "board":"****x****", "player":"o" }]'

    # Output:
    #    [
    #        {
    #            "indexes":[
    #                8,
    #                6,
    #                2,
    #                0,
    #                7,
    #                5,
    #                3,
    #                1
    #            ]
    #        }
    #    ]
```

The tic-tac-toe board is indexed as:

0 1 2

3 4 5

6 7 8


Tests can be run with:
```bash
    $ python tests.py
```


## Web service version

I used flask to implement a small web service. Flask and its dependencies can be installed with either of the following:
```bash
    $ pip install flask
```
or
```bash
    $ pip install -r requirements.txt
```

After installing flask, the server can be run with the line:
```bash
   $ python server.py 
```

The server can be queried at: http://localhost:5000/next-move?board=*********&player=x

```bash
    curl -i "http://localhost:5000/next-move?board=*********&player=x"
```
