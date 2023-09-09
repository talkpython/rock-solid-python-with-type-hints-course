import random
from typing import Optional

# You can inline this of course, but it's used in multiple places and
# is fairly complex, so I'm giving it a name here:
BoardType = list[list[Optional[str]]]


def main():
    print()
    print("Welcome to 4-in-row from TALK PYTHON")
    print()

    # CREATE THE BOARD:
    # Board is a list of rows
    # Rows are a list of cells
    board: BoardType = [  # See BoardType definition at the top of the file.
        # 6 rows
        [None, None, None, None, None, None, None],  # 7 columns per row
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    # CHOOSE INITIAL PLAYER
    # We could use X and O, but let's liven it
    # up with some emoji from: https://emojipedia.org/baseball/
    symbols: list[str] = ["🏀", "🥎"]

    active_player_index: int = 0
    player_name: str = input("What is your name player 1? ")
    players: list[str] = [player_name.capitalize(), "Computer"]
    print(f"Welcome {players[0]}")
    print(f"Your symbol will be {symbols[0]}.")
    print(f"{players[1]}, will be {symbols[1]}.")
    player = players[active_player_index]
    symbol = symbols[active_player_index]

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player: str = players[active_player_index]
        symbol: str = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol, active_player_index == 1):
            print("That isn't an option, try again.")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index: int = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} ({symbol}) has won with the board: ")
    show_board(board)
    print()


def choose_location(board: BoardType, symbol: str, is_computer: bool) -> bool:
    if not is_computer:
        column = int(input("Choose which column: "))
    else:
        column = random.randint(1, len(board[0]))
        print(f"Computer chooses column {column}")

    column -= 1
    if column < 0 or column >= len(board[0]):
        return False

    row = find_bottom_row(board, column)
    if row is None:
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def find_bottom_row(board: BoardType, column: int) -> Optional[int]:
    col_cells: list[str] = [
        board[n][column]
        for n in range(0, len(board))
    ]

    last_empty: Optional[int] = None
    for idx, cell in enumerate(col_cells):
        if cell is None:
            last_empty = idx

    return last_empty


def show_board(board: BoardType):
    for row_idx, row in enumerate(board, start=1):
        print("| ", end='')
        for col_idx, cell in enumerate(row, start=1):
            empty_text = f"({row_idx}, {col_idx})"
            symbol = f'  {cell}   ' if cell is not None else empty_text
            print(symbol, end=" | ")
        print()


def announce_turn(player: str):
    print()
    print(f"It's {player}'s turn. Here's the board:")
    print()


def find_winner(board: BoardType):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board: BoardType):
    sequences = []

    # Win by rows.
    rows = board
    for row in rows:
        # Go through each row and get any consecutive sequence of 4 cells
        fours_across = find_sequences_of_four_cells_in_a_row(row)
        sequences.extend(fours_across)

    # Win by columns
    for col_idx in range(0, 7):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
            board[3][col_idx],
            board[4][col_idx],
            board[5][col_idx],
        ]
        # Go through each column and get any consecutive sequence of 4 cells
        fours_down = find_sequences_of_four_cells_in_a_row(col)
        sequences.extend(fours_down)

    # Win by diagonals
    # In Tic-Tac-Toe, we just had two diagonals, and they were easy to compute.
    # It's pretty simple here too, but more, so just a bit more to type out
    # for the possible options.
    #
    # To help visualize this, here is the board with indices: (row,col)
    # [
    #     ['(0,0)', '(0,1)', '(0,2)', '(0,3)', '(0,4)', '(0,5)', '(0,6)'],
    #     ['(1,0)', '(1,1)', '(1,2)', '(1,3)', '(1,4)', '(1,5)', '(1,6)'],
    #     ['(2,0)', '(2,1)', '(2,2)', '(2,3)', '(2,4)', '(2,5)', '(2,6)'],
    #     ['(3,0)', '(3,1)', '(3,2)', '(3,3)', '(3,4)', '(3,5)', '(3,6)'],
    #     ['(4,0)', '(4,1)', '(4,2)', '(4,3)', '(4,4)', '(4,5)', '(4,6)'],
    #     ['(5,0)', '(5,1)', '(5,2)', '(5,3)', '(5,4)', '(5,5)', '(5,6)'],
    #     ]
    #
    # I'm sure there a clever double for i in range(0, rows) & for j in range(0, cols)
    # solution. But I'm afraid it will be too confusing for lots of us.
    # So I'll just do it long-hand down here.
    diagonals: list[list[Optional[str]]] = [  # <-- Could be BoardType, but they are not intrinsically
        # linked structurally and could deviate

        # Down to the right diagonals
        [board[5][0]],  # Not really used, too short, but here for building the pattern
        [board[4][0], board[5][1]],  # Not really used, too short, but here for building the pattern
        [board[3][0], board[4][1], board[5][2]],  # Not really used, too short, but here for building the pattern
        [board[2][0], board[3][1], board[4][2], board[5][3]],
        [board[1][0], board[2][1], board[3][2], board[4][3], board[5][4]],
        [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5]],
        [board[0][1], board[1][2], board[2][3], board[3][4], board[4][5], board[5][6]],
        [board[0][2], board[1][3], board[2][4], board[3][5], board[4][6]],
        [board[0][3], board[1][4], board[2][5], board[3][6]],
        [board[0][4], board[1][5], board[2][6]],  # Not really used, too short, but here for building the pattern
        [board[0][5], board[1][6]],  # Not really used, too short, but here for building the pattern
        [board[0][6]],  # Not really used, too short, but here for building the pattern

        # Down to the left diagonals
        [board[0][0]],  # Not really used, too short, but here for building the pattern
        [board[0][1], board[1][0]],  # Not really used, too short, but here for building the pattern
        [board[2][0], board[1][1], board[0][2]],  # Not really used, too short, but here for building the pattern
        [board[0][3], board[1][2], board[2][1], board[3][0]],
        [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]],
        [board[0][5], board[1][4], board[2][3], board[3][2], board[4][1], board[5][0]],
        [board[0][6], board[1][5], board[2][4], board[3][3], board[4][2], board[5][1]],
        [board[1][6], board[2][5], board[3][4], board[4][3], board[5][2]],
        [board[2][6], board[3][5], board[4][4], board[5][3]],
        [board[3][6], board[4][5], board[5][4]],  # Not really used, too short, but here for building the pattern
        [board[4][6], board[5][5]],  # Not really used, too short, but here for building the pattern
        [board[5][6]],  # Not really used, too short, but here for building the pattern
    ]
    for diag in diagonals:
        fours_diagonals = find_sequences_of_four_cells_in_a_row(diag)
        sequences.extend(fours_diagonals)

    return sequences


def find_sequences_of_four_cells_in_a_row(cells: list[str]) -> list[list[str]]:
    sequences: list[list[str]] = []  # <-- Could be BoardType, but they are not intrinsically
    # linked structurally and could deviate

    for n in range(0, len(cells) - 3):
        candidate = cells[n:n + 4]
        if len(candidate) == 4:
            sequences.append(candidate)

    return sequences


if __name__ == '__main__':
    main()
