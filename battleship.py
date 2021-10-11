# Author: Anupam Sushil
# Battleship


import random

### DO NOT EDIT BELOW (with the exception of MAX_MISSES) ###

HIT_CHAR = 'x'
MISS_CHAR = 'o'
BLANK_CHAR = '.'
HORIZONTAL = 'h'
VERTICAL = 'v'
MAX_MISSES = 20
SHIP_SIZES = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
NUM_ROWS = 10
NUM_COLS = 10
ROW_IDX = 0
COL_IDX = 1
MIN_ROW_LABEL = 'A'
MAX_ROW_LABEL = 'J'


def get_random_position():
    """Generates a random location on a board of NUM_ROWS x NUM_COLS."""

    row_choice = chr(
                    random.choice(
                        range(
                            ord(MIN_ROW_LABEL),
                            ord(MIN_ROW_LABEL) + NUM_ROWS
                        )
                    )
    )

    col_choice = random.randint(0, NUM_COLS - 1)

    return (row_choice, col_choice)


def play_battleship():
    """Controls flow of Battleship games including display of
    welcome and goodbye messages.

    :return: None
    """

    print("Let's Play Battleship!\n")

    game_over = False

    while not game_over:

        game = Game()
        game.display_board()

        while not game.is_complete():
            pos = game.get_guess()
            result = game.check_guess(pos)
            game.update_game(result, pos)
            game.display_board()

        game_over = end_program()

    print("Goodbye.")

### DO NOT EDIT ABOVE (with the exception of MAX_MISSES) ###


class Ship:

    def __init__(self, name, start_position, orientation):
        #enables initialization of Ship instance
        """Creates a new ship with the given name, placed at start_position in the
        provided orientation. The number of positions occupied by the ship is determined
        by looking up the name in the SHIP_SIZE dictionary.

        :param name: the name of the ship
        :param start_position: tuple representing the starting position of ship on the board
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return: None
        """
        self.name = name
        num_positions = SHIP_SIZES[name]
        positions = {start_position: False}
        row = start_position[ROW_IDX]
        col = start_position[COL_IDX]
        if orientation == VERTICAL:
            row_as_num = ord(row)
            for position in range(num_positions - 1):
                row_as_num += 1
                row = chr(row_as_num)
                positions[(row, col)] = False
        else:
            for position in range(num_positions - 1):
                col += 1
                positions[(row, col)] = False
        self.positions = positions
        self.sunk = False





class Game:

    ########## DO NOT EDIT #########
    
    _ship_types = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    
    
    def display_board(self):
        """ Displays the current state of the board."""

        print()
        print("  " + ' '.join('{}'.format(i) for i in range(len(self.board))))
        for row_label in self.board.keys():
            print('{} '.format(row_label) + ' '.join(self.board[row_label]))
        print()

    ########## DO NOT EDIT #########

    def __init__(self, max_misses = MAX_MISSES):
        #enables initialization of Game instance
        """ Creates a new game with max_misses possible missed guesses.
        The board is initialized in this function and ships are randomly
        placed on the board.

        :param max_misses: maximum number of misses allowed before game ends
        """
        self.max_misses = max_misses
        self.ships = []
        self.guesses = []
        self.board = {}
        self.initialize_board()
        self.create_and_place_ships()

    def initialize_board(self):
        #sets board attribute to full of dots
        """Sets the board to it's initial state with each position occupied by
        a period ('.') string.

        :return: None
        """
        for row in "ABCDEFGHIJ":
            self.board[row] =[BLANK_CHAR] * NUM_COLS

    def in_bounds(self, start_position, ship_size, orientation):
        #Ships cannot be outside of the boundaries of the board; Returns True if a ship can be placed
        # by satisfying this conditions
        """Checks that a ship requiring ship_size positions can be placed at start position.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement inside board boundary, False otherwise
        """
        row = start_position[ROW_IDX]
        col = start_position[COL_IDX]
        if orientation == VERTICAL:
            highest_row = chr(ord(row) + ship_size - 1)
            if highest_row <= MAX_ROW_LABEL:
                return True
            else:
                return False
        else:
            highest_col = col + ship_size -1
            if highest_col <= NUM_COLS -1:
                return True
            else:
                return False

    def overlaps_ship(self, start_position, ship_size, orientation):
        #A newly placed ship cannot overlap with a ship that has already been placed; Returns True if a ship can be placed
        # by satisfying this conditions
        """Checks for overlap between previously placed ships and a potential new ship
        placement requiring ship_size positions beginning at start_position in the
        given orientation.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement overlaps previously placed ship, False otherwise
        """
        row = start_position[ROW_IDX]
        col = start_position[COL_IDX]
        position_list = [(row, col)]
        if orientation == VERTICAL:
            position_as_num = ord(row)
            for position in range(ship_size - 1):
                position_as_num += 1
                row = chr(position_as_num)
                position_list.append((row, col ))
        else:
            for position in range(ship_size - 1):
                col += 1
                position_list.append((row, col))

        for ship in self.ships:
            for positions in ship.positions:
                if positions in position_list:
                    return True

        return False

    def place_ship(self, start_position, ship_size):
        #makes function calls to in_bounds() and overlaps_ship() to see if you can place a ship
        """Determines if placement is possible for ship requiring ship_size positions placed at
        start_position. Returns the orientation where placement is possible or None if no placement
        in either orientation is possible.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :return orientation: 'h' if horizontal placement possible, 'v' if vertical placement possible,
            None if no placement possible
        """
        if self.in_bounds(start_position, ship_size, HORIZONTAL) and not self.overlaps_ship(start_position, ship_size, HORIZONTAL):
            return HORIZONTAL
        elif self.in_bounds(start_position, ship_size, VERTICAL) and not self.overlaps_ship(start_position, ship_size, VERTICAL):
            return VERTICAL
        else:
            return None

    def create_and_place_ships(self):
        #creates the game's ships and places those ships on the board. Handles randomly placing ships by the use of the
        #get_random_position helper function given to us
        """Instantiates ship objects with valid board placements.

        :return: None
        """
        for ship in self._ship_types:
            orientation = None
            while orientation == None:
                start_position = get_random_position()
                ship_size = SHIP_SIZES[ship]
                orientation = self.place_ship(start_position, ship_size)
            ship_instance = Ship(ship, start_position, orientation)
            self.ships.append(ship_instance)

    def get_guess(self):
        #logic for getting a valid position value from the user
        """Prompts the user for a row and column to attack. The
        return value is a board position in (row, column) format

        :return position: a board position as a (row, column) tuple
        """

        row = input("Enter a row: ")
        while row not in "ABCDEFGHIJ":
            row = input("Enter a row: ")
        column = int(input("Enter a column: "))
        while column not in list(range(NUM_COLS)):
            column = int(input("Enter a column: "))
        return (row, column)

    def check_guess(self, position):
        #Registering a hit requires updating the value for the ship's positions dict to True at the
        #position (the key of the dict) where the hit occurs, and printing a message
        """Checks whether or not position is occupied by a ship. A hit is
        registered when position occupied by a ship and position not hit
        previously. A miss occurs otherwise.

        :param position: a (row,column) tuple guessed by user
        :return: guess_status: True when guess results in hit, False when guess results in miss
        """
        for ship in self.ships:
            for occupied_position in ship.positions:
                if position == occupied_position and ship.positions[occupied_position] != True:
                    ship.positions[occupied_position] = True
                    ship.sunk = True
                    print("You sunk the {}!".format(ship.name))
                    return True
        return False

    def update_game(self, guess_status, position):
        #When the user's guess results in a hit, the board is updated. When the user's guess is a miss,
        #the board attribute and the guesses attribute are both updated
        """Updates the game by modifying the board with a hit or miss
        symbol based on guess_status of position.

        :param guess_status: True when position is a hit, False otherwise
        :param position:  a (row,column) tuple guessed by user
        :return: None
        """
        if guess_status:
            self.board[position[ROW_IDX]][position[COL_IDX]] = "x"
        else:
            self.guesses.append(position)
            if self.board[position[ROW_IDX]][position[COL_IDX]] == ".":
                self.board[position[ROW_IDX]][position[COL_IDX]] = "o"


    def is_complete(self):
        #1-All ships on the board are sunk
        #2-The number of missed guesses by the user reaches the maximum allowed number of misses
        #returns True if any of the 2 above conditions satisfied
        """Checks to see if a Battleship game has ended. Returns True when the game is complete
        with a message indicating whether the game ended due to successfully sinking all ships
        or reaching the maximum number of guesses. Returns False when the game is not
        complete.

        :return: True on game completion, False otherwise
        """
        sunked_ships = []
        for ship in self.ships:
            if ship.sunk:
                sunked_ships.append(ship)
        if len(sunked_ships) == len(self.ships):
            print("YOU WIN!")
            return True
        elif len(self.guesses) >= self.max_misses:
            print("SORRY! NO GUESSES LEFT.")
            return True
        return False



def end_program():
    #handles logic for playing more than one session
    """Prompts the user with "Play again (Y/N)?" The question is repeated
    until the user enters a valid response (Y/y/N/n). The function returns
    False if the user enters 'Y' or 'y' and returns True if the user enters
    'N' or 'n'.

    :return response: boolean indicating whether to end the program
    """

    play_again = input("Play again (Y/N)? ")
    while play_again not in "YyNn":
        play_again = input("Play again (Y/N)? ")
    if play_again in "Yy":
        return False
    else:
        return True


def main():
    #highest node in program
    """Executes one or more games of Battleship."""

    play_battleship()


if __name__ == "__main__":
    main()
