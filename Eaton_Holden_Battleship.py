import time
import random

def print_board(board):
    print(f'''
    1   2   3   4   5
1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
-------------------------
2 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]}
-------------------------
3 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}
-------------------------
4 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]}
-------------------------
5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}
    ''')

def place_bot_dots(board):
    dots = []

    for i in range(4):
        row = random.randint(0,4)
        col = random.randint(0,4)

        if board[row][col] != '🔵':
            continue
        board[row][col] = '🛥️'
        dots.append([row, col])
        print_board(board)
    return dots

def place_player_dots(board):
    dots = []

    for i in range(4):
        row = int(input(f'Enter row for ship #{i+1}: ')) - 1
        col = int(input(f'Enter column for ship #{i+1}: ')) - 1
        
        if board[row][col] != '🔵':
            continue
        board[row][col] = '🛥️'
        dots.append((row, col))
        print_board(board)
    return dots

def player_shot(board, hidden_board, shots):
    row = int(input("Enter row: ")) - 1
    col = int(input("Enter column: ")) - 1

    if hidden_board[row][col] == '🛥️':
        print("that is a hit!!")
        board[row][col] = '💥'
    else:
        print("that is a miss!!")
        board[row][col] = '🌊'
    shots.append([row, col])
    print_board(board)

def bot_shot(board, hidden_board, shots):
    row = random.randint(0,4)
    col = random.randint(0,4)

    if hidden_board[row][col] == '🛥️':
        print("Bot got a hit!!")
        board[row][col] = '💥'
    else:
        print("Bot missed!!")
        board[row][col] = '🌊'
    shots.append([row, col])
    print_board(board)

def check_winner(bot_board):
    shots = 0
    for list in bot_board:
        for dot in list:
            if dot == '💥':
                shots += 1
    if shots == 4:
        return True
    
    ''''''
    #return True/False based on whether dots is a subset of shots (look up: how to determine if one list is a subset of another in python)

def main(): 
    player_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]

    player_hidden_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]

    bot_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]

    bot_hidden_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]

    bot_shots = []
    player_shots = []
    
    print('Bot is placing dots...')
    bot_dots = place_bot_dots(bot_board)
    print('Time to place your dots!')
    player_dots = place_player_dots(player_board)

    while True:
        print('Bot takes a shot!')
        bot_shot(player_board, player_hidden_board, bot_shots)

        if check_winner(player_board):
              print('Bot Wins!')
        

        print('Player take a shot')
        player_shot(bot_board, bot_hidden_board, player_shots)

        if check_winner(bot_board):
              print('player Wins!')
            
        time.sleep(3)

main()