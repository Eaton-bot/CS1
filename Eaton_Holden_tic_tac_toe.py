
def display_board(board): # Prints the tic tac toe board
      print (f"""
1  {board[0][0]} | {board[0][1]} | {board[0][2]}
-----------
2 {board[1][0]} | {board[1][1]} | {board[1][2]}
-----------
3 {board[2][0]} | {board[2][1]} | {board[2][2]}



""")

def player_move(board, player): # Handles a player's move

      while True:
            while True: ## Keeps asking until a valid move is made
                  try:  # Ask player for column and subtract 1
                        # because list indexes start at 0
                        column = int(input(f'Player {player} which column do you want (1, 2 or 3): ')) - 1
                           # Ask player for row
                        row = int(input(f'Player {player} which row do you want (1, 2 or 3): ')) - 1
                        # Checks if row/column are outside board range
                        if column > 2 or column < 0 or row > 2 or row < 0:
                              print('Please only enter numbers between 1 and 3.')
                        else:
                              break
                         # Run if player enters something that is not a number
                  except ValueError:
                        print('Please enter an integer!')

            if board[row][column] == ' ':  # Checks if chosen spot is empty
                  # Places player's symbol on board
                  board[int(row)][int(column)] = player
                  break
            else:
                  print('spot taken')
                  continue

                  

def is_draw(board): # Checks if the game is a draw
      if board [0][0] == ' ' or board [0][1] == ' ' or board [0][2] == ' ' or board [1][0]  or board [1][1] == ' '  or board [1][2] == ' '   or board [2][0] == ' 'or board [2][1] == ' '  or board [2][2] == ' ':
            # if ANY spot is empty, game is not a draw yet
            return False
      return True
             # If no spaces left, it's a draw

def check_winner_board(board): ## Checks if someone won the game
      while True:
               # Top row win for x
            if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
                  print('x has won the game')
                  return True
                     # Top row win for o
            elif board[0][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                  print('o has won the game')
                  return True
             # Middle row win for x
            if board[1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
                  print('x has won the game')
                  return True
             # Middle row win for o
            elif board[1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                  print('o has won the game')
                  return True
            if board[2][0] == 'x' and board [2][1] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            # Bottom row win for x
            elif board[2][2] == 'o' and board [2][1] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
             # Bottom row win for o
            elif board[0][0] == 'x' and board [1][0] == 'x' and board [2][0] == 'x':
                  print('x has won the game')
                  return True
             # Left column win for x
            elif board[0][0] == 'o' and board [1][0] == 'o' and board [2][0] == 'o':
                  print('o has won the game')
                  return True
                # Left column win for o
            elif board [0][1] == 'x' and board [1][1] == 'x' and board [2][1] == 'x':
                  print('x has won the game')
                  return True
              # Middle column win for x
            elif board [0][1] == 'o' and board [1][1] == 'o' and board [2][1] == 'o':
                  print('o has won the game')
                  return True
            # Middle column win for o
            elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            # Right column win for x
            elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'x':
                  print('o has won the game')
                  return True
            # Right column win for o
            elif board [0][0] == 'x' and board [1][1] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            # Diagonal win top-left to bottom-right for x
            elif board [0][0] == 'o' and board [1][1] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            # Diagonal win top-left to bottom-right for o
            elif board [2][0] == 'x' and board [1][1] == 'x' and board [0][2] == 'x':
                  print('x has won the game')
                  return True
             # Diagonal win (bottom-left to top-right) for x
            elif board [2][0] == 'o' and board [1][1] == 'o' and board [0][2] == 'o':
                  print('o has won the game')
                  return True
            # Diagonal win (bottom-left to top-right) for o
            elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            # Diagonal win (bottom-left to top-right) for x
            elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            else:     # No winner found
                  return False
                                                                                    

def main(): # Main game function
      while True:
           # Allows game replay



            board = [[" "," "," ",],
                  [" "," "," ",],
                  [" "," "," ",]]
                        # Creates empty game board
                         # Lets player 1 choose x or o
            while True:
                  player1 = input('Player 1, x or o? ')

                  if player1 in ['x', 'o']:
                        if player1 == 'x':
                              player2 = 'o'
                              break
                        else:
                              player2 = 'x'
                              break

            while True:   # Main game loop
                  display_board(board)  # Display board
                  player_move(board, player1) # Player 1 move

                  if check_winner_board(board):  # Check if player 1 won
                        print("Player 1 wins!")
                        break
                  display_board(board) 
                  # Show updated board
                  if is_draw(board):  # Check for draw
                        print("game is a ties")
                        break
                  player_move(board, player2)  # Player 2 move
                  
                  if check_winner_board(board): # Check if player 2 won
                        print("Player 2 wins!")
                        break

            play_again = input("do you want to play again(y,n)") # Ask to play again
            if play_again == 'n':   # Ends game if player types n
                  break
main()
        
