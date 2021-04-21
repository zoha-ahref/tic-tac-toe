board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
user = True
turns = 0


def printBoard(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


def quit(user_input):
    if user_input.lower() == "q":
        print("Thank you for playing")
        return True
    else:
        return False


def check_input(user_input):
    #check if input is a number
    if not is_num(user_input):
        return False
    user_input = int(user_input)
    #check if between 1 - 9 range
    if not is_bounds(user_input):
        return False
    return True


def is_num(user_input):
    if not user_input.isnumeric():
        print("This is not a valid input")
        return False
    else:
        return True


def is_bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else:
        return True





def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is taken")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diagnol(user, board):
        return True
    return False


def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False


def check_diagnol(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


while turns < 9:
    active_user = current_user(user)
    printBoard(board)
    user_input = input("Enter a number through 1 to 9 or enter \"q\" to quit.")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break

    turns += 1
    if turns == 9:
        print("Tie")
    user = not user
