
def display_board(board):
      print (f"""
1  {board[0][0]} | {board[0][1]} | {board[0][2]}
-----------
2 {board[1][0]} | {board[1][1]} | {board[1][2]}
-----------
3 {board[2][0]} | {board[2][1]} | {board[2][2]}



""")

def player_move(board, player):
      while True:
            while True:
                  try:
                        column = int(input(f'Player {player} which column do you want (1, 2 or 3): ')) - 1
                        row = int(input(f'Player {player} which row do you want (1, 2 or 3): ')) - 1

                        if column > 2 or column < 0 or row > 2 or row < 0:
                              print('Please only enter numbers between 1 and 3.')
                        else:
                              break
                  except ValueError:
                        print('Please enter an integer!')

            if board[row][column] == ' ':
                  board[int(row)][int(column)] = player
                  break
            else:
                  print('spot taken')
                  continue

                  

def is_draw(board):
      if board [0][0] == ' ' or board [0][1] == ' ' or board [0][2] == ' ' or board [1][0]  or board [1][1] == ' '  or board [1][2] == ' '   or board [2][0] == ' 'or board [2][1] == ' '  or board [2][2] == ' ':
            return False
      return True
           

def check_winner_board(board):
      while True:
            if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
                  print('x has won the game')
                  return True
            elif board[0][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                  print('o has won the game')
                  return True
            if board[1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
                  print('x has won the game')
                  return True
            elif board[1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                  print('o has won the game')
                  return True
            if board[2][0] == 'x' and board [2][1] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board[2][2] == 'o' and board [2][1] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            elif board[0][0] == 'x' and board [1][0] == 'x' and board [2][0] == 'x':
                  print('x has won the game')
                  return True
            elif board[0][0] == 'o' and board [1][0] == 'o' and board [2][0] == 'o':
                  print('o has won the game')
                  return True
            elif board [0][1] == 'x' and board [1][1] == 'x' and board [2][1] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][1] == 'o' and board [1][1] == 'o' and board [2][1] == 'o':
                  print('o has won the game')
                  return True
            elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'x':
                  print('o has won the game')
                  return True
            elif board [0][0] == 'x' and board [1][1] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][0] == 'o' and board [1][1] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            elif board [2][0] == 'x' and board [1][1] == 'x' and board [0][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [2][0] == 'o' and board [1][1] == 'o' and board [0][2] == 'o':
                  print('o has won the game')
                  return True
            elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            else:
                  return False
                                                                                    

def main():
      while True:
           



            board = [[" "," "," ",],
                  [" "," "," ",],
                  [" "," "," ",]]
            
            while True:
                  player1 = input('Player 1, x or o? ')

                  if player1 in ['x', 'o']:
                        if player1 == 'x':
                              player2 = 'o'
                              break
                        else:
                              player2 = 'x'
                              break

            while True:
                  display_board(board)
                  player_move(board, player1)

                  if check_winner_board(board):
                        print("Player 1 wins!")
                        break
                  display_board(board)
                  if is_draw(board):
                        print("game is a ties")
                        break
                  player_move(board, player2)
                  
                  if check_winner_board(board):
                        print("Player 2 wins!")
                        break

            play_again = input("do you want to play again(y,n)")
            if play_again == 'n':
                  break
main()
        