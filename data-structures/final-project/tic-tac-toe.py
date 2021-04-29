# Dictionary used to build our board, taking the shape of the number pad on a keyboard.
board = {
  '7': ' ',
  '8': ' ',
  '9': ' ',
  '4': ' ',
  '5': ' ',
  '6': ' ',
  '1': ' ',
  '2': ' ',
  '3': ' '
}

# maintain a list of keys for reference 
board_keys = []

for key in board:
    board_keys.append(key)

def print_board(board):
    print('{0}|{1}|{2}'.format(board['7'], board['8'], board['9']))
    print('-+-+-')
    print('{0}|{1}|{2}'.format(board['4'], board['5'], board['6']))
    print('-+-+-')
    print('{0}|{1}|{2}'.format(board['1'], board['2'], board['3']))

# Basic function to check for match across rows, columns and diagonals
def check_for_win(square_one, square_two, square_three):
    if board[square_one] == board[square_two] == board[square_three]:
        return True
    else:
        return False

def print_winning_message(winner):
    print_board(board)
    print('Game over, {0} won'.format(winner))

def play_game():
    print('Welcome to Tic Tac Toe! The board matches the number pad on your keyboard.')

    turn = 'X'
    move_count = 0

  # loop through the range(10) for nine possible moves
    
    for i in range(10):
        print_board(board)
        move = input('It\'s {0}\'s turn. What space do you pick? '.format(turn))

        if board[move] == ' ':
            #place the character on the board
            board[move] = turn
            #increment our count of turns
            move_count = move_count + 1

        else:
            print('That space is taken. Pick a different space')
            # continue through the loop
            continue
    
        # Start checking for wins after 5 moves.
        if move_count >= 5:
            #check each row
            if check_for_win('7', '8', '9'):
                print_winning_message(turn)
                # if a win happens, we break out of the loop
                break
            elif check_for_win('4', '5', '6'):
                print_winning_message(turn)
                break
            elif check_for_win('1', '2', '3'):
                print_winning_message(turn)
                break
            #check each column
            elif check_for_win('7', '4', '1'):
                print_winning_message(turn)
                break
            elif check_for_win('8', '5', '2'):
                print_winning_message(turn)
                break
            elif check_for_win('9', '6', '3'):
                print_winning_message(turn)
                break
            # check two diagonals
            elif check_for_win('7', '5', '3'):
                print_winning_message(turn)
                break
            elif check_for_win('1', '5', '9'):
                print_winning_message(turn)
                break
        # If we get to 9 moves without a win, the game is tied. 
        if move_count == 9:
            print('Game over, tie game')
            break
        # alternate players
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    play_again = input('Would you like to play again? Y/N: ')

    if play_again.upper() == 'Y':
        # clear out the board to start again
        for key in board_keys:
            board[key] = ' '
        play_game()  
          
    else:
        print('thanks for playing')

play_game()

