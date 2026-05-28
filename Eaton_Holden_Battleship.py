import time
import random

def print_board(board):
      #Creates a function that prints the game board.
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
#Displays the 5x5 board with row and column labels
def place_bot_dots(board):
    #Creates a function that randomly places the bot’s ships
    dots = []
    #Creates an empty list to store ship coordinates
    i = 0

    while i < 4:
        #Runs until 4 ships are placed
        row = random.randint(0,4)
        #Picks a random row
        col = random.randint(0,4)
        #Picks a random column.

        if board[row][col] != '🔵':
            #Checks if a ship is already there
            continue
        board[row][col] = '🛥️'
         # a ship on the
        dots.append([row, col])
        #Saves the ship coordinates
        print_board(board)
        i += 1 #Increases the ship counter
    return dots

def place_player_dots(board): #Creates a function for the player to place ships manually
    dots = []

    i = 0

    while i < 4:
        row = int(input(f'Enter row for ship #{i+1}: ')) - 1
            #Gets the row from the user and converts it to list indexing
        col = int(input(f'Enter column for ship #{i+1}: ')) - 1
        #Gets the column from the user
        
        if board[row][col] != '🔵': #Prevents ships from overlapping
            continue
        board[row][col] = '🛥️'
        dots.append((row, col)) #Saves the ship location
        print_board(board)
        i += 1
    return dots

def player_shot(board, hidden_board, shots):
    #function for the player attacking the bot
    row = int(input("Enter row: ")) - 1 #Gets attack row from player
    col = int(input("Enter column: ")) - 1 #Gets attack column from player

    if hidden_board[row][col] == '🛥️':
        print("that is a hit!!")
        board[row][col] = '💥' #Marks a hit
    else:
        print("that is a miss!!")
        board[row][col] = '🌊' #Marks a miss
    shots.append([row, col])  #Stores the shot coordinates
    print_board(board)

def bot_shot(board, hidden_board, shots):
    row = random.randint(0,4) #Bot randomly chooses coordinates
    col = random.randint(0,4)

    if hidden_board[row][col] == '🛥️': #Checks if bot hit a ship
        print("Bot got a hit!!")
        board[row][col] = '💥' #Marks hit location
    else:
        print("Bot missed!!")
        board[row][col] = '🌊' #Marks miss location
    shots.append([row, col])
    print_board(board)

def check_winner(bot_board): #Checks if all ships have been destroyed
    shots = 0
    for list in bot_board: #Loops through each row
        for dot in list: #Loops through each spot in the row
            if dot == '💥': #Checks for hit markers
                shots += 1
    if shots == 4: #Checks if all 4 ships are hit
        return True
    
    ''''''
    
def main():  #Main function that runs the game
    player_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]
#Creates the player's visible board
    player_hidden_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]
#Creates hidden player ship board
    bot_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]
#Creates bot visible board
    bot_hidden_board = [
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ["🔵","🔵","🔵","🔵","🔵"],
    ]
#Creates hidden bot ship board
    bot_shots = [] #Stores bot attack history
    player_shots = [] #Stores player attack history
    
    print('Bot is placing dots...') #Displays setup message
    bot_dots = place_bot_dots(bot_board) #Places bot ships
    print('Time to place your dots!')
    player_dots = place_player_dots(player_board) #Lets player place ships

    while True: #Main game loop that repeats forever
        print('Bot takes a shot!')
        bot_shot(player_board, player_hidden_board, bot_shots)
            #Bot attacks player
        if check_winner(player_board): #Checks if bot won
              print('Bot Wins!')
        

        print('Player take a shot') #Displays winner message
        player_shot(bot_board, bot_hidden_board, player_shots) #Player attacks bot

        if check_winner(bot_board): #Checks if player won
              print('player Wins!') #Displays winner message
            
        time.sleep(3) #Pauses game for 3 seconds

main()
