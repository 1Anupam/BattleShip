Battleship

Battleship is a famous two-player board game. Each player is given 5 ships: a Carrier, a Battleship, a Cruiser, a Submarine, and Destroyer. The objective of Battleship is to be the first player to sink the other player's 5 ships. The first player to sink the opponent's ships wins. Each ship occupies a specific number of positions on the board: Carrier (5 spaces), Battleship (4 spaces), Cruiser (3 spaces), Submarine (3 spaces), and Destroyer (2 spaces). Before the game begins, each player places the 5 ships on the board. Once the game starts, the ships cannot be moved. Neither player can see the placement of the opponent's ships. The real-world Battleship game provides two boards for each player. A lower (horizontal) board is where the player places their 5 ships. An upper (vertical) board is where the player records guesses have been made to track where to guess in future turns.

The following rules restrict ship placement:

- All 5 ships must be placed on the board.
- Ships can only be placed vertically or horizontally on the board; diagonal placement is not allowed.
- No ship can hang off the board.
- No ship can overlap another on the board.

Both players are supplied with red and white pegs. Players take turns calling out board coordinates. When a coordinate called out by a player represents a position on the opponent's board where a ship has been placed, the opponent responds "hit". Otherwise, the opponent responds "miss". The player will mark a _miss_ with a white peg when a _miss_ occurs. A red peg is used when a _hit_ occurs. The opponent places a red peg on the ship when a _hit_ occurs. The opponent makes no peg placement after a _miss_.

When a ship has red pegs in all holes, the ship is sunk. The opponent must announce "hit and sunk" in this case. The game ends when all of the ships of one player have all been sunk.

Battleship.py is a simplified version of this game. Only one player is involved in the game. Ship placement follows the rules above but is managed by the program (not by a player). The player does not need to manage placement of ships, therefore, the board only reflects the results of the coordinate guesses of an attack. The player can only miss on 20 (`MAX_MISSES`) coordinate guesses during the course of the game. If the player sinks all ships before exhausting this number of guesses, the player wins. Otherwise, the player loses.

This game heavily uses Objected-Oriented Programming (OOP). `Ship` and `Game` are Python classes. The different types of ships are instances (objects) of the `Ship` class. A single instance of the `Game` class is used in the program.

To play the game, just run battleship.py
