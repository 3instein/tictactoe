import random

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }


def init():
    player = input("X/O? ")
    if player == "X" or player == "O":
        return player
    else:
        init()

def print_board(state):
    for i in range(3):
        for j in range(3):
            if type(state[i][j]) == int:
                print("[ ]", end="")
            else:
                print("[" + str(state[i][j]) + "]", end="")
        print("")

def turn(state):
    x = 0; o = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == "X":
                x += 1
            elif state[i][j] == "O":
                o += 1
    if x == o:
        return True
    else:
        return False

def terminal(state):
    print("\n" * 100)
    print_board(board)
    for i in range(3):
        if state[i][0] == "X" and state[i][1] == "X" and state[i][2] == "X":
            print(utility(state))
            return True
        if state[i][0] == "O" and state[i][1] == "O" and state[i][2] == "O":
            print(utility(state))
            return True

    for i in range(3):
        if state[0][i] == "X" and state[1][i] == "X" and state[2][i] == "X":
            print(utility(state))
            return True
        if state[0][i] == "O" and state[1][i] == "O" and state[2][i] == "O":
            print(utility(state))
            return True

    if state[0][0] == "X" and state[1][1] == "X" and state[2][2] == "X"\
        or state[0][2] == "X" and state[1][1] == "X" and state[2][0] == "X":
        print(utility(state))
        return True

    if state[0][0] == "O" and state[1][1] == "O" and state[2][2] == "O"\
        or state[0][2] == "O" and state[1][1] == "O" and state[2][0] == "O":
        print(utility(state))
        return True

    if not actions(state):
        print(utility(state))
        return True

    return False

def result(state, action, player):
    x,y = action[0],action[1]

    state[x][y] = player

    return state

def utility(state):
    for i in range(3):
        if state[i][0] == player and state[i][1] == player and state[i][2] == player:
            return -1
        if state[i][0] == bot and state[i][1] == bot and state[i][2] == bot:
            return 1

    for i in range(3):
        if state[0][i] == player and state[1][i] == player and state[2][i] == player:
            return -1
        if state[0][i] == bot and state[1][i] == bot and state[2][i] == bot:
            return 1

    if state[0][0] == player and state[1][1] == player and state[2][2] == player \
            or state[0][2] == player and state[1][1] == player and state[2][0] == player:
        return -1

    if state[0][0] == bot and state[1][1] == bot and state[2][2] == bot \
            or state[0][2] == bot and state[1][1] == bot and state[2][0] == bot:
        return 1

    return 0

def actions(state):
    cells = []

    for i in range(3):
        for j in range(3):
            if type(state[i][j]) == int:
                cells.append([i,j])

    return cells

player = init()
if player == "X":
    bot = "O"
else:
    bot = "X"
while(not terminal(board)):
    if turn(board) and player == "X" or not turn(board) and player == "O":
        action = input("Action? ")
        action = [action[0],action[2]]
        if type(board[int(action[0])][int(action[1])]) == int:
            x,y = int(action[0]), int(action[1])
            board = result(board, [x,y], player)
    elif turn(board) and player != "X" or not turn(board) and player != "O":

        if type(board[1][1]) == int:
            board = result(board, [1,1], bot)
        elif board[0][0] == 0:
            board = result(board, [0,0], bot)
        elif board[0][2] == 0:
            board = result(board, [0, 2], bot)
        elif board[2][0] == 0:
            board = result(board, [2, 0], bot)
        elif board[2][2] == 0:
            board = result(board, [2, 2], bot)
        else:
            row = random.randint(0, 2)
            cell = random.randint(0, 2)

            x, y = row, cell
            board = result(board, [x, y], bot)


